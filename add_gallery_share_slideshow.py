from pathlib import Path
import re

script_add = """
<script id="gallery-share-slideshow-js">
let slideTimer=null;

function sharePhoto(){
  const a=document.getElementById("lbDownload");
  const title=document.getElementById("lbTitle") ? document.getElementById("lbTitle").innerText : "KALD Archive Photo";
  if(!a)return;
  const url=a.href;
  if(navigator.share){
    navigator.share({title:title,url:url}).catch(()=>{});
  }else{
    navigator.clipboard.writeText(url);
    alert("Photo link copied.");
  }
}

function toggleSlideshow(){
  const btn=document.getElementById("slideBtn");
  if(slideTimer){
    clearInterval(slideTimer);
    slideTimer=null;
    if(btn)btn.innerText="Play";
  }else{
    slideTimer=setInterval(()=>{ nextPhoto(); },3000);
    if(btn)btn.innerText="Pause";
  }
}

const oldClose=window.closeLightbox;
window.closeLightbox=function(){
  if(slideTimer){clearInterval(slideTimer);slideTimer=null;}
  const btn=document.getElementById("slideBtn");
  if(btn)btn.innerText="Play";
  if(oldClose)oldClose();
}
</script>
"""

for p in Path(".").glob("photos-*.html"):
    text=p.read_text(encoding="utf-8", errors="ignore")

    if 'onclick="sharePhoto()"' not in text:
        text=text.replace(
            '<a id="lbDownload" href="#" download>Download</a>',
            '<button onclick="sharePhoto()">Share</button><button id="slideBtn" onclick="toggleSlideshow()">Play</button><a id="lbDownload" href="#" download>Download</a>'
        )

    text=re.sub(r'<script id="gallery-share-slideshow-js">.*?</script>', '', text, flags=re.S)
    text=text.replace("</body>", script_add + "\n</body>")

    p.write_text(text, encoding="utf-8")
    print("Added share/slideshow:", p.name)

print("Done.")
