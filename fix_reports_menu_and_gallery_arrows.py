from pathlib import Path
import re

# 1. Force reports.html mobile viewport + menu
p = Path("reports.html")
text = p.read_text(encoding="utf-8", errors="ignore")

if '<meta name="viewport"' not in text:
    text = text.replace("<head>", '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">')

text = re.sub(r'<nav>.*?</nav>', '''
<nav>
<a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a>
<button class="menu-btn" onclick="toggleMenu()">MENU</button>
<div class="nav-links" id="navLinks">
<a href="index.html">Home</a>
<a href="dashboard.html">Dashboard</a>
<a href="photos.html">Photos</a>
<a href="videos.html">Videos</a>
<a href="documents.html">Documents</a>
<a href="reports.html">Reports</a>
<a href="archive-status.html">Status</a>
</div>
</nav>
''', text, count=1, flags=re.S)

fix_css = '''
<style id="force-reports-mobile-menu">
@media(max-width:768px){
  nav{padding:12px 14px!important;display:flex!important;flex-direction:row!important;align-items:center!important;justify-content:space-between!important;flex-wrap:wrap!important}
  .brand{max-width:72%!important;font-size:14px!important;line-height:1.1!important}
  .brand img{height:38px!important}
  .brand span{font-size:18px!important}
  .menu-btn{display:block!important;background:#0b4f8a!important;color:#fff!important;border:0!important;border-radius:12px!important;padding:10px 16px!important;font-weight:900!important}
  .nav-links{display:none!important;width:100%!important;flex-direction:column!important;gap:7px!important;margin-top:12px!important;margin-left:0!important}
  .nav-links.show{display:flex!important}
  .nav-links a{width:100%!important;box-sizing:border-box!important;text-align:center!important;background:#eef6fc!important;color:#0b4f8a!important;padding:10px!important;border-radius:10px!important;font-size:14px!important}
}
</style>
<script id="force-reports-menu-script">
function toggleMenu(){
  const nav=document.getElementById("navLinks");
  if(nav){nav.classList.toggle("show");}
}
</script>
'''

text = re.sub(r'<style id="force-reports-mobile-menu">.*?</style>', '', text, flags=re.S)
text = re.sub(r'<script id="force-reports-menu-script">.*?</script>', '', text, flags=re.S)
text = text.replace("</head>", fix_css + "\n</head>")

p.write_text(text, encoding="utf-8")
print("Fixed reports mobile menu")

# 2. Fix photo viewer left/right arrows on all photo pages
viewer_css = '''
<style id="viewer-arrow-mobile-fix">
.lbNav{
  z-index:100005!important;
  opacity:1!important;
  visibility:visible!important;
}
.lbPrev{
  left:10px!important;
}
.lbNext{
  right:10px!important;
}
@media(max-width:768px){
  .lbPrev{
    left:8px!important;
  }
  .lbNext{
    right:8px!important;
  }
  .lbNav{
    top:55%!important;
    font-size:26px!important;
    padding:11px 15px!important;
    background:#0b6fae!important;
    color:#fff!important;
    box-shadow:0 4px 14px #0008!important;
  }
  .lightbox img{
    max-width:92%!important;
    max-height:60vh!important;
  }
}
</style>
'''

for f in Path(".").glob("photos-*.html"):
    html = f.read_text(encoding="utf-8", errors="ignore")
    html = re.sub(r'<style id="viewer-arrow-mobile-fix">.*?</style>', '', html, flags=re.S)
    html = html.replace("</head>", viewer_css + "\n</head>")
    f.write_text(html, encoding="utf-8")
    print("Fixed viewer arrows:", f.name)

print("Done.")
