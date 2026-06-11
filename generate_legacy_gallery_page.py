from pathlib import Path

thumb_dir = Path("assets/thumbsLegacy")
photos = sorted(thumb_dir.glob("*.jpg"))

cards = []
for photo in photos:
    name = photo.stem
    src = photo.as_posix()
    cards.append(f'''
<div class="photo">
  <img loading="lazy" src="{src}" alt="{name}">
  <p>{name}</p>
</div>''')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Legacy Photo Collection</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1b2a3a}}
nav{{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}}
.brand img{{height:52px}}
.nav-links{{display:flex;align-items:center;gap:18px;margin-left:auto}}
.nav-links a{{text-decoration:none;color:#0b4f8a;font-weight:700}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:55px 25px}}
.actions,.searchPanel{{max-width:1150px;margin:25px auto 0;padding:0 25px}}
.btn{{display:inline-block;background:#0b4f8a;color:white;text-decoration:none;padding:12px 18px;border-radius:10px;font-weight:700}}
.searchPanel{{display:flex;gap:12px;align-items:center;flex-wrap:wrap}}
.searchPanel input{{flex:1;min-width:240px;padding:14px;border:1px solid #ccd6e0;border-radius:12px;font-size:16px}}
.searchPanel .count{{font-weight:800;color:#0b4f8a}}
.gallery{{max-width:1150px;margin:auto;padding:25px;display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px}}
.photo{{background:white;border-radius:14px;box-shadow:0 4px 12px #0003;overflow:hidden;cursor:pointer;transition:.2s}}
.photo:hover{{transform:translateY(-3px);box-shadow:0 8px 24px #0004}}
.photo img{{width:100%;height:170px;object-fit:cover;display:block;cursor:pointer}}
.photo p{{margin:0;padding:8px;text-align:center;font-size:13px;font-weight:700;color:#0b4f8a}}
.viewer{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:9999;align-items:center;justify-content:center;flex-direction:column}}
.viewer.show{{display:flex}}
.viewer img{{max-width:90%;max-height:75vh;transition:.2s}}
.viewer .topbar{{position:absolute;top:15px;left:20px;right:20px;display:flex;justify-content:space-between;align-items:center;color:white;font-weight:700}}
.viewer button{{background:#0b6fae;color:white;border:0;border-radius:10px;padding:10px 14px;font-weight:700;margin:4px;cursor:pointer}}
.viewer .navbtn{{position:absolute;top:50%;transform:translateY(-50%);font-size:28px}}
.viewer .prev{{left:20px}}
.viewer .next{{right:20px}}
#backTop{{position:fixed;right:18px;bottom:18px;background:#0b4f8a;color:white;border:0;border-radius:50px;padding:12px 16px;font-weight:700;display:none;z-index:999;cursor:pointer}}
footer{{text-align:center;background:#102a43;color:white;padding:25px;margin-top:35px}}
@media(max-width:760px){{nav{{padding:12px 14px;flex-wrap:wrap}}.brand{{width:100%;justify-content:center;margin-bottom:8px}}.nav-links{{width:100%;justify-content:center;flex-wrap:wrap;gap:12px}}.nav-links a{{font-size:14px}}.gallery{{grid-template-columns:repeat(auto-fit,minmax(125px,1fr));gap:12px;padding:12px}}.photo img{{height:125px}}.viewer .topbar{{display:block;text-align:center}}.viewer button{{font-size:12px;padding:9px 10px}}}}
</style>
</head>
<body>
<nav><a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a><div class="nav-links"><a href="index.html">Home</a><a href="dashboard.html">Dashboard</a><a href="about.html">About</a><a href="photos.html">Photos</a><a href="videos.html">Videos</a><a href="documents.html">Documents</a><a href="reports.html">Reports</a></div></nav>
<section class="hero"><h1>Legacy Photo Collection</h1><p>1,300 recovered photos from legacy USB media, pending final event classification.</p></section>
<div class="actions"><a class="btn" href="photos.html">Back to Photos</a></div>
<div class="searchPanel"><input id="searchBox" type="text" placeholder="Search photo name"><span class="count" id="photoCount">Showing {len(photos)} photos</span></div>
<div class="gallery">
{''.join(cards)}
</div>

<div class="viewer" id="viewer">
  <div class="topbar">
    <span id="counter">Photo 1 of 1</span>
    <div><button onclick="zoomIn()">Zoom +</button><button onclick="zoomOut()">Zoom -</button><button onclick="closeViewer()">X Close</button></div>
  </div>
  <button class="navbtn prev" onclick="prevPhoto()">&#10094;</button>
  <img id="viewerImg" src="">
  <button class="navbtn next" onclick="nextPhoto()">&#10095;</button>
</div>
<button id="backTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">Top</button>

<script>
let photos=[],visiblePhotos=[],current=0,zoom=1,touchStartX=0,touchEndX=0;
document.addEventListener("DOMContentLoaded",()=>{{
  photos=[...document.querySelectorAll(".photo")];
  visiblePhotos=[...photos];
  photos.forEach(card=>card.querySelector("img").addEventListener("click",()=>openViewerByCard(card)));
  document.getElementById("searchBox").addEventListener("input",function(){{
    const q=this.value.toLowerCase().trim();let visible=0;
    photos.forEach(card=>{{const show=card.innerText.toLowerCase().includes(q);card.style.display=show?"":"none";if(show)visible++;}});
    visiblePhotos=photos.filter(c=>c.style.display!=="none");
    document.getElementById("photoCount").textContent="Showing "+visible+" of "+photos.length+" photos";
  }});
  window.addEventListener("scroll",()=>{{document.getElementById("backTop").style.display=scrollY>400?"block":"none"}});
  document.addEventListener("keydown",e=>{{if(e.key==="Escape")closeViewer();if(e.key==="ArrowLeft")prevPhoto();if(e.key==="ArrowRight")nextPhoto();}});
  const viewerBox=document.getElementById("viewer");
  viewerBox.addEventListener("touchstart",e=>touchStartX=e.changedTouches[0].screenX,false);
  viewerBox.addEventListener("touchend",e=>{{touchEndX=e.changedTouches[0].screenX;handleSwipe();}},false);
}});
function openViewerByCard(card){{visiblePhotos=photos.filter(c=>c.style.display!=="none");current=visiblePhotos.indexOf(card);zoom=1;updateViewer();document.getElementById("viewer").classList.add("show")}}
function closeViewer(){{document.getElementById("viewer").classList.remove("show")}}
function updateViewer(){{const img=visiblePhotos[current].querySelector("img");document.getElementById("viewerImg").src=img.src.replace("assets/thumbsLegacy/","assets/mediumLegacy/");document.getElementById("viewerImg").style.transform="scale("+zoom+")";document.getElementById("counter").textContent="Photo "+(current+1)+" of "+visiblePhotos.length+" - "+img.alt;}}
function prevPhoto(){{if(!visiblePhotos.length)return;current=(current-1+visiblePhotos.length)%visiblePhotos.length;zoom=1;updateViewer()}}
function nextPhoto(){{if(!visiblePhotos.length)return;current=(current+1)%visiblePhotos.length;zoom=1;updateViewer()}}
function zoomIn(){{zoom=Math.min(3,zoom+.25);updateViewer()}}
function zoomOut(){{zoom=Math.max(.6,zoom-.25);updateViewer()}}
function handleSwipe(){{const diff=touchEndX-touchStartX;if(Math.abs(diff)<50)return;if(diff<0)nextPhoto();else prevPhoto();}}
</script>
<footer><p>KALD Digital Archive Center | Legacy Photo Collection</p></footer>
</body>
</html>'''

Path("photos-legacy.html").write_text(html, encoding="utf-8")
print(f"Generated photos-legacy.html with {len(photos)} photos.")
