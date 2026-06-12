from pathlib import Path
import re, html

nav_html = '''
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
<style id="clean-global-nav">
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
  .nav-links a{width:100%!important;box-sizing:border-box!important;text-align:center!important;background:#eef6fc!important;padding:10px!important;border-radius:10px!important;font-size:14px!important}
}
</style>
'''

script = '''
<script id="clean-global-menu-script">
function toggleMenu(){
  const nav=document.getElementById("navLinks");
  if(nav){nav.classList.toggle("show");}
}
</script>
'''

for p in Path(".").glob("*.html"):
    text = p.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r'<nav>.*?</nav>', nav_html, text, count=1, flags=re.S)
    text = re.sub(r'<style id="clean-global-nav">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<style id="pro-mobile-header">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<style id="hamburger-menu-css">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<style id="final-mobile-polish">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="clean-global-menu-script">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<script id="pro-menu-script">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<script id="menu-script">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<script id="final-mobile-menu-script">.*?</script>', '', text, flags=re.S)
    text = text.replace("</head>", css + "\n</head>")
    text = text.replace("</body>", script + "\n</body>")
    p.write_text(text, encoding="utf-8")
    print("Fixed nav:", p.name)

# rebuild document actions safely
doc = Path("documents.html")
text = doc.read_text(encoding="utf-8", errors="ignore")

def fix_actions(m):
    dtype = m.group(1)
    name = m.group(2)
    size = m.group(4)
    action = m.group(5)
    href = re.search(r'href="([^"]+)"', action)
    if not href:
        return m.group(0)
    path = href.group(1)
    if "docs.google.com" in path:
        old = re.search(r'url=([^"&]+)', path)
        if old:
            path = old.group(1)
    if dtype == "PDF":
        buttons = f'<a class="btn" href="{path}" target="_blank" rel="noopener">View PDF</a> <a class="btn" href="{path}" download>Download</a>'
    else:
        buttons = f'<span style="color:#777;font-weight:700">Preview not available</span> <a class="btn" href="{path}" download>Download</a>'
    return f'<tr data-type="{dtype}">\n<td>{name}</td>\n<td>{dtype}</td>\n<td>{size}</td>\n<td>{buttons}</td>\n</tr>'

text = re.sub(
    r'<tr data-type="([^"]+)">\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>',
    fix_actions,
    text,
    flags=re.S
)

# remove desktop.ini row
text = re.sub(r'<tr data-type="Other">.*?desktop\.ini.*?</tr>', '', text, flags=re.S)

doc.write_text(text, encoding="utf-8")
print("Fixed documents preview actions.")

