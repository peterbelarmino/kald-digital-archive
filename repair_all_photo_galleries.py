from pathlib import Path
import re

pages = list(Path(".").glob("photos-*.html"))

css = """
<style id="gallery-repair-css">
.lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,.94);z-index:99999;align-items:center;justify-content:center;flex-direction:column}
.lightbox.show{display:flex}
.lightbox img{max-width:94%;max-height:76vh;box-shadow:0 0 30px #000}
.lbTop{position:absolute;top:10px;left:10px;right:10px;display:flex;justify-content:space-between;align-items:center;color:#fff;font-weight:800}
.lbBtns button,.lbBtns a{background:#0b6fae;color:white;border:0;border-radius:10px;padding:9px 12px;margin:3px;font-weight:800;text-decoration:none}
.lbNav{position:absolute;top:50%;transform:translateY(-50%);background:#0b6fae;color:white;border:0;border-radius:50%;font-size:28px;padding:10px 15px}
.lbPrev{left:10px}.lbNext{right:10px}
.lbCount{position:absolute;bottom:12px;color:white;background:#0008;padding:8px 14px;border-radius:20px;font-weight:800}
@media(max-width:768px){
  .lightbox img{max-width:96%;max-height:66vh}
  .lbTop{flex-direction:column;gap:8px;text-align:center}
  .lbBtns button,.lbBtns a{font-size:12px;padding:8px 10px}
}
</style>
"""

html = """
<div class="lightbox" id="lightbox">
  <div class="lbTop">
    <div id="lbTitle">KALD Photo</div>
    <div class="lbBtns">
      <button onclick="zoomIn()">Zoom +</button>
      <button onclick="zoomOut()">Zoom -</button>
      <a id="lbDownload" href="#" download>Download</a>
      <button onclick="closeLightbox()">Close</button>
    </div>
  </div>
  <button class="lbNav lbPrev" onclick="prevPhoto()">&#10094;</button>
  <img id="lbImg" src="">
  <button class="lbNav lbNext" onclick="nextPhoto()">&#10095;</button>
  <div class="lbCount" id="lbCount">Photo 1 of 1</div>
</div>
"""

js = """
<script id="gallery-repair-js">
let galleryItems=[],currentIndex=0,zoomLevel=1;

document.addEventListener("DOMContentLoaded",function(){
  galleryItems=[...document.querySelectorAll(".photo a")];

  galleryItems.forEach((a,i)=>{
    a.addEventListener("click",function(e){
      e.preventDefault();
      currentIndex=i;
      zoomLevel=1;
      openLightbox();
    });
  });

  document.addEventListener("keydown",function(e){
    const box=document.getElementById("lightbox");
    if(!box || !box.classList.contains("show")) return;
    if(e.key==="Escape") closeLightbox();
    if(e.key==="ArrowLeft") prevPhoto();
    if(e.key==="ArrowRight") nextPhoto();
  });
});

function openLightbox(){
  updateLightbox();
  document.getElementById("lightbox").classList.add("show");
  document.body.style.overflow="hidden";
}

function closeLightbox(){
  document.getElementById("lightbox").classList.remove("show");
  document.body.style.overflow="";
}

function updateLightbox(){
  if(!galleryItems.length)return;
  const a=galleryItems[currentIndex];
  const card=a.closest(".photo");
  const label=card && card.querySelector("p") ? card.querySelector("p").innerText : "Photo";
  const title=document.querySelector(".hero h1") ? document.querySelector(".hero h1").innerText : "KALD Photo";

  document.getElementById("lbImg").src=a.getAttribute("href");
  document.getElementById("lbImg").style.transform="scale("+zoomLevel+")";
  document.getElementById("lbTitle").innerText=title+" | "+label;
  document.getElementById("lbCount").innerText="Photo "+(currentIndex+1)+" of "+galleryItems.length;
  document.getElementById("lbDownload").href=a.getAttribute("href");
}

function nextPhoto(){
  currentIndex=(currentIndex+1)%galleryItems.length;
  zoomLevel=1;
  updateLightbox();
}

function prevPhoto(){
  currentIndex=(currentIndex-1+galleryItems.length)%galleryItems.length;
  zoomLevel=1;
  updateLightbox();
}

function zoomIn(){
  zoomLevel=Math.min(3,zoomLevel+.25);
  updateLightbox();
}

function zoomOut(){
  zoomLevel=Math.max(.5,zoomLevel-.25);
  updateLightbox();
}
</script>
"""

for p in pages:
    text = p.read_text(encoding="utf-8", errors="ignore")

    # remove old broken viewers/scripts
    text = re.sub(r'<style id="photo-viewer-pro-css">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="photo-viewer-pro-js">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<style id="gallery-repair-css">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="gallery-repair-js">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<div class="lightbox" id="lightbox">.*?</div>\s*', '', text, flags=re.S)

    # clean duplicate target attributes
    text = re.sub(r'\s*target="_blank"\s*rel="noopener"', '', text)

    text = text.replace("</head>", css + "\n</head>")
    text = text.replace("</body>", html + "\n" + js + "\n</body>")

    p.write_text(text, encoding="utf-8")
    print("Fixed gallery:", p.name)

print("All photo galleries repaired.")
