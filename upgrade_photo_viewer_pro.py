from pathlib import Path
import re

gallery_pages = [
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
"photos-2017.html",
"photos-2019.html",
"photos-legacy.html"
]

css = """
<style id="photo-viewer-pro-css">
.viewer{display:none;position:fixed;inset:0;background:rgba(0,0,0,.94);z-index:99999;align-items:center;justify-content:center;flex-direction:column}
.viewer.show{display:flex}
.viewer img{max-width:92%;max-height:72vh;transition:.2s ease;box-shadow:0 0 30px #000}
.viewerTop{position:absolute;top:12px;left:14px;right:14px;display:flex;justify-content:space-between;align-items:center;color:white;gap:10px}
.viewerTitle{font-weight:800;font-size:15px}
.viewerBtns{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.viewer button,.viewer a.viewerBtn{background:#0b6fae;color:white;border:0;border-radius:10px;padding:9px 12px;font-weight:800;text-decoration:none;cursor:pointer;font-size:13px}
.viewer button:hover,.viewer a.viewerBtn:hover{background:#083d6b}
.viewerNav{position:absolute;top:50%;transform:translateY(-50%);font-size:34px;border-radius:50%!important;padding:12px 16px!important}
.viewerPrev{left:18px}
.viewerNext{right:18px}
.viewerCounter{position:absolute;bottom:14px;color:white;font-weight:800;background:rgba(0,0,0,.45);padding:8px 14px;border-radius:20px}
.searchPanel{max-width:1150px;margin:auto;padding:12px 20px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.searchPanel input{flex:1;min-width:240px;padding:13px;border:1px solid #ccd6e0;border-radius:12px;font-size:16px}
.count{font-weight:800;color:#0b4f8a}
#backTop{position:fixed;right:18px;bottom:18px;background:#0b4f8a;color:white;border:0;border-radius:50px;padding:12px 16px;font-weight:800;display:none;z-index:999;cursor:pointer}
body.viewer-open{overflow:hidden}
@media(max-width:768px){
  .viewerTop{flex-direction:column;align-items:stretch;text-align:center}
  .viewerBtns{justify-content:center}
  .viewer button,.viewer a.viewerBtn{padding:8px 10px;font-size:12px}
  .viewer img{max-width:96%;max-height:62vh}
  .viewerNav{font-size:24px!important;padding:10px 13px!important}
  .viewerPrev{left:6px}
  .viewerNext{right:6px}
  .viewerCounter{bottom:10px;font-size:13px}
}
</style>
"""

viewer = """
<div class="viewer" id="viewer">
  <div class="viewerTop">
    <div class="viewerTitle" id="viewerTitle">KALD Archive Photo</div>
    <div class="viewerBtns">
      <button onclick="zoomIn()">Zoom +</button>
      <button onclick="zoomOut()">Zoom -</button>
      <button onclick="toggleFullScreen()">Full</button>
      <a class="viewerBtn" id="downloadBtn" href="#" download>Download</a>
      <button onclick="closeViewer()">Close</button>
    </div>
  </div>
  <button class="viewerNav viewerPrev" onclick="prevPhoto()">&#10094;</button>
  <img id="viewerImg" src="" alt="">
  <button class="viewerNav viewerNext" onclick="nextPhoto()">&#10095;</button>
  <div class="viewerCounter" id="viewerCounter">Photo 1 of 1</div>
</div>
<button id="backTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">Top</button>
"""

script = """
<script id="photo-viewer-pro-js">
let photos=[],visiblePhotos=[],current=0,zoom=1,touchStartX=0,touchEndX=0,lastTap=0;

document.addEventListener("DOMContentLoaded",()=>{
  photos=[...document.querySelectorAll(".photo")];
  visiblePhotos=[...photos];

  photos.forEach((card)=>{
    const a=card.querySelector("a");
    if(a){
      a.addEventListener("click",(e)=>{
        e.preventDefault();
        visiblePhotos=photos.filter(c=>c.style.display!=="none");
        current=visiblePhotos.indexOf(card);
        zoom=1;
        openViewer();
      });
    }
  });

  const search=document.getElementById("searchBox");
  if(search){
    search.addEventListener("input",()=>{
      const q=search.value.toLowerCase().trim();
      let count=0;
      photos.forEach(card=>{
        const show=card.innerText.toLowerCase().includes(q);
        card.style.display=show?"":"none";
        if(show)count++;
      });
      visiblePhotos=photos.filter(c=>c.style.display!=="none");
      const pc=document.getElementById("photoCount");
      if(pc){pc.textContent="Showing "+count+" of "+photos.length+" photos";}
    });
  }

  window.addEventListener("scroll",()=>{
    const b=document.getElementById("backTop");
    if(b){b.style.display=scrollY>400?"block":"none";}
  });

  document.addEventListener("keydown",(e)=>{
    const viewer=document.getElementById("viewer");
    if(!viewer || !viewer.classList.contains("show"))return;
    if(e.key==="Escape")closeViewer();
    if(e.key==="ArrowLeft")prevPhoto();
    if(e.key==="ArrowRight")nextPhoto();
    if(e.key==="+" || e.key==="=")zoomIn();
    if(e.key==="-" || e.key==="_")zoomOut();
  });

  const viewer=document.getElementById("viewer");
  if(viewer){
    viewer.addEventListener("touchstart",e=>{
      touchStartX=e.changedTouches[0].screenX;
    },false);
    viewer.addEventListener("touchend",e=>{
      touchEndX=e.changedTouches[0].screenX;
      const now=new Date().getTime();
      if(now-lastTap<300){ zoom = zoom===1 ? 2 : 1; updateViewer(); }
      lastTap=now;
      handleSwipe();
    },false);
  }
});

function openViewer(){
  updateViewer();
  document.getElementById("viewer").classList.add("show");
  document.body.classList.add("viewer-open");
}

function closeViewer(){
  document.getElementById("viewer").classList.remove("show");
  document.body.classList.remove("viewer-open");
}

function updateViewer(){
  if(!visiblePhotos.length)return;
  const card=visiblePhotos[current];
  const a=card.querySelector("a");
  const img=card.querySelector("img");
  const label=card.querySelector("p") ? card.querySelector("p").innerText : "Photo";
  const pageTitle=document.querySelector(".hero h1") ? document.querySelector(".hero h1").innerText : "KALD Archive Photo";

  document.getElementById("viewerImg").src=a.href;
  document.getElementById("viewerImg").style.transform="scale("+zoom+")";
  document.getElementById("viewerTitle").textContent=pageTitle+" | "+label;
  document.getElementById("viewerCounter").textContent="Photo "+(current+1)+" of "+visiblePhotos.length;
  document.getElementById("downloadBtn").href=a.href;
}

function prevPhoto(){ if(!visiblePhotos.length)return; current=(current-1+visiblePhotos.length)%visiblePhotos.length; zoom=1; updateViewer(); }
function nextPhoto(){ if(!visiblePhotos.length)return; current=(current+1)%visiblePhotos.length; zoom=1; updateViewer(); }
function zoomIn(){ zoom=Math.min(3,zoom+.25); updateViewer(); }
function zoomOut(){ zoom=Math.max(.5,zoom-.25); updateViewer(); }

function toggleFullScreen(){
  const viewer=document.getElementById("viewer");
  if(!document.fullscreenElement){ viewer.requestFullscreen?.(); }
  else{ document.exitFullscreen?.(); }
}

function handleSwipe(){
  const diff=touchEndX-touchStartX;
  if(Math.abs(diff)<60)return;
  if(diff<0)nextPhoto();else prevPhoto();
}
</script>
"""

for page in gallery_pages:
    p=Path(page)
    if not p.exists():
        continue

    text=p.read_text(encoding="utf-8", errors="ignore")

    text=re.sub(r'<style id="photo-viewer-pro-css">.*?</style>', '', text, flags=re.S)
    text=re.sub(r'<script id="photo-viewer-pro-js">.*?</script>', '', text, flags=re.S)
    text=re.sub(r'<div class="viewer" id="viewer">.*?</div>\s*<button id="backTop".*?</button>', '', text, flags=re.S)

    if 'id="searchBox"' not in text:
        count=len(re.findall(r'<div class="photo"', text))
        text=text.replace(
            '<section class="gallery">',
            f'<div class="searchPanel"><input id="searchBox" type="text" placeholder="Search photo name"><span class="count" id="photoCount">Showing {count} photos</span></div><section class="gallery">'
        )

    text=text.replace("</head>", css + "\n</head>")
    text=text.replace("<footer>", viewer + "\n<footer>")
    text=text.replace("</body>", script + "\n</body>")

    p.write_text(text, encoding="utf-8")
    print("Viewer Pro upgraded:", page)

print("Done Photo Viewer Pro upgrade.")
