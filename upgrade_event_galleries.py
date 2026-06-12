from pathlib import Path
import re

pages = [
"photos-2016-apr13.html",
"photos-2016-sep21.html",
"photos-2016-nov01.html",
"photos-2016-dec03.html",
"photos-2017-mar11.html",
"photos-2020-feb15.html",
"photos-2021-jan12.html",
"photos-2021-jan18.html",
"photos-2021-jan25.html",
"photos-2021-oct09.html",
"photos-mrs-amal.html",
"photos-conference-formal.html",
]

extra_css = """
.searchPanel{max-width:1150px;margin:auto;padding:10px 20px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.searchPanel input{flex:1;min-width:240px;padding:13px;border:1px solid #ccd6e0;border-radius:12px;font-size:16px}
.count{font-weight:800;color:#0b4f8a}
.viewer{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:9999;align-items:center;justify-content:center;flex-direction:column}
.viewer.show{display:flex}
.viewer img{max-width:90%;max-height:75vh;transition:.2s}
.viewer .topbar{position:absolute;top:15px;left:20px;right:20px;display:flex;justify-content:space-between;align-items:center;color:white;font-weight:700}
.viewer button{background:#0b6fae;color:white;border:0;border-radius:10px;padding:10px 14px;font-weight:700;margin:4px;cursor:pointer}
.viewer .navbtn{position:absolute;top:50%;transform:translateY(-50%);font-size:28px}
.viewer .prev{left:20px}.viewer .next{right:20px}
#backTop{position:fixed;right:18px;bottom:18px;background:#0b4f8a;color:white;border:0;border-radius:50px;padding:12px 16px;font-weight:700;display:none;z-index:999;cursor:pointer}
"""

viewer_html = """
<div class="viewer" id="viewer">
  <div class="topbar">
    <span id="counter">Photo 1 of 1</span>
    <div>
      <button onclick="zoomIn()">Zoom +</button>
      <button onclick="zoomOut()">Zoom -</button>
      <button onclick="closeViewer()">X Close</button>
    </div>
  </div>
  <button class="navbtn prev" onclick="prevPhoto()">&#10094;</button>
  <img id="viewerImg" src="">
  <button class="navbtn next" onclick="nextPhoto()">&#10095;</button>
</div>
<button id="backTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">Top</button>
"""

script = """
<script>
let photos=[],visiblePhotos=[],current=0,zoom=1,touchStartX=0,touchEndX=0;
document.addEventListener("DOMContentLoaded",()=>{
  photos=[...document.querySelectorAll(".photo")];
  visiblePhotos=[...photos];

  photos.forEach(card=>{
    const a=card.querySelector("a");
    if(a){
      a.addEventListener("click",(e)=>{
        e.preventDefault();
        openViewerByCard(card);
      });
    }
  });

  const search=document.getElementById("searchBox");
  if(search){
    search.addEventListener("input",function(){
      const q=this.value.toLowerCase().trim();
      let visible=0;
      photos.forEach(card=>{
        const show=card.innerText.toLowerCase().includes(q);
        card.style.display=show?"":"none";
        if(show)visible++;
      });
      visiblePhotos=photos.filter(c=>c.style.display!=="none");
      document.getElementById("photoCount").textContent="Showing "+visible+" of "+photos.length+" photos";
    });
  }

  window.addEventListener("scroll",()=>{
    document.getElementById("backTop").style.display=scrollY>400?"block":"none";
  });

  document.addEventListener("keydown",e=>{
    if(e.key==="Escape")closeViewer();
    if(e.key==="ArrowLeft")prevPhoto();
    if(e.key==="ArrowRight")nextPhoto();
  });

  const viewerBox=document.getElementById("viewer");
  viewerBox.addEventListener("touchstart",e=>touchStartX=e.changedTouches[0].screenX,false);
  viewerBox.addEventListener("touchend",e=>{
    touchEndX=e.changedTouches[0].screenX;
    handleSwipe();
  },false);
});

function openViewerByCard(card){
  visiblePhotos=photos.filter(c=>c.style.display!=="none");
  current=visiblePhotos.indexOf(card);
  zoom=1;
  updateViewer();
  document.getElementById("viewer").classList.add("show");
}
function closeViewer(){document.getElementById("viewer").classList.remove("show")}
function updateViewer(){
  if(!visiblePhotos.length)return;
  const a=visiblePhotos[current].querySelector("a");
  const img=visiblePhotos[current].querySelector("img");
  document.getElementById("viewerImg").src=a.href;
  document.getElementById("viewerImg").style.transform="scale("+zoom+")";
  document.getElementById("counter").textContent="Photo "+(current+1)+" of "+visiblePhotos.length+" - "+(img.alt || "");
}
function prevPhoto(){if(!visiblePhotos.length)return;current=(current-1+visiblePhotos.length)%visiblePhotos.length;zoom=1;updateViewer()}
function nextPhoto(){if(!visiblePhotos.length)return;current=(current+1)%visiblePhotos.length;zoom=1;updateViewer()}
function zoomIn(){zoom=Math.min(3,zoom+.25);updateViewer()}
function zoomOut(){zoom=Math.max(.6,zoom-.25);updateViewer()}
function handleSwipe(){
  const diff=touchEndX-touchStartX;
  if(Math.abs(diff)<50)return;
  if(diff<0)nextPhoto();else prevPhoto();
}
</script>
"""

for page in pages:
    p=Path(page)
    text=p.read_text(encoding="utf-8")

    if ".viewer{" not in text:
        text=text.replace("</style>", extra_css + "\n</style>")

    count=len(re.findall(r'<div class="photo"', text))

    if 'id="searchBox"' not in text:
        text=text.replace(
            '<section class="gallery">',
            f'<div class="searchPanel"><input id="searchBox" type="text" placeholder="Search photo name"><span class="count" id="photoCount">Showing {count} photos</span></div><section class="gallery">'
        )

    if 'id="viewer"' not in text:
        text=text.replace("<footer>", viewer_html + "\n<footer>")

    if "function openViewerByCard" not in text:
        text=text.replace("</body>", script + "\n</body>")

    # add alt if missing
    text=re.sub(r'<img loading="lazy" src="([^"]+)">', r'<img loading="lazy" src="\1" alt="Photo">', text)

    p.write_text(text, encoding="utf-8")
    print("Upgraded", page, count)

print("Done upgrading event galleries.")
