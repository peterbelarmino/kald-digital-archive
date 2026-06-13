from pathlib import Path
import re

p = Path("reports.html")
text = p.read_text(encoding="utf-8", errors="ignore")

nav = '''
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
'''

css = '''
<style id="reports-nav-fix">
nav{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}
.brand{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}
.brand img{height:52px}
.nav-links{display:flex;gap:18px;margin-left:auto}
.nav-links a{text-decoration:none;color:#0b4f8a;font-weight:700}
.menu-btn{display:none;background:#0b4f8a;color:white;border:0;border-radius:10px;padding:10px 16px;font-weight:800;cursor:pointer}
@media(max-width:768px){
nav{padding:12px 14px!important;flex-direction:row!important;align-items:center!important;justify-content:space-between!important;flex-wrap:wrap!important}
.brand{max-width:72%!important;font-size:14px!important;line-height:1.1!important}
.brand img{height:38px!important}
.brand span{font-size:18px!important}
.menu-btn{display:block!important}
.nav-links{display:none!important;width:100%!important;flex-direction:column!important;gap:7px!important;margin-top:12px!important;margin-left:0!important}
.nav-links.show{display:flex!important}
.nav-links a{width:100%!important;box-sizing:border-box!important;text-align:center!important;background:#eef6fc!important;color:#0b4f8a!important;padding:10px!important;border-radius:10px!important;font-size:14px!important}
}
</style>
'''

script = '''
<script id="reports-menu-script">
function toggleMenu(){
  const nav=document.getElementById("navLinks");
  if(nav){nav.classList.toggle("show");}
}
</script>
'''

text = re.sub(r'<nav>.*?</nav>', nav, text, count=1, flags=re.S)
text = re.sub(r'<style id="reports-nav-fix">.*?</style>', '', text, flags=re.S)
text = re.sub(r'<script id="reports-menu-script">.*?</script>', '', text, flags=re.S)

text = text.replace("</head>", css + "\n</head>")
text = text.replace("</body>", script + "\n</body>")

p.write_text(text, encoding="utf-8")
print("reports.html menu fixed")
