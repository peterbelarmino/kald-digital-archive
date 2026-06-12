from pathlib import Path
import re

header_css = """
<style id="pro-mobile-header">
.menu-btn{
  display:none;
  background:#0b4f8a;
  color:white;
  border:0;
  border-radius:10px;
  padding:10px 14px;
  font-weight:800;
  cursor:pointer;
  margin-left:auto;
}
@media(max-width:768px){
  nav{
    padding:12px 14px!important;
    flex-direction:row!important;
    align-items:center!important;
    justify-content:space-between!important;
    flex-wrap:wrap!important;
  }
  .brand{
    width:auto!important;
    max-width:78%!important;
    font-size:16px!important;
    line-height:1.15!important;
  }
  .brand img{
    height:42px!important;
  }
  .menu-btn{
    display:block!important;
    width:auto!important;
    margin:0!important;
    font-size:14px!important;
  }
  .nav-links{
    display:none!important;
    width:100%!important;
    flex-direction:column!important;
    gap:8px!important;
    margin-left:0!important;
    margin-top:12px!important;
  }
  .nav-links.show{
    display:flex!important;
  }
  .nav-links a{
    width:100%!important;
    box-sizing:border-box!important;
    text-align:center!important;
    background:#eef6fc!important;
    padding:10px!important;
    border-radius:10px!important;
    font-size:14px!important;
  }
}
</style>
"""

script = """
<script id="pro-menu-script">
function toggleMenu(){
  const nav=document.getElementById("navLinks");
  if(nav){nav.classList.toggle("show");}
}
</script>
"""

for p in Path(".").glob("*.html"):
    text = p.read_text(encoding="utf-8", errors="ignore")

    # remove old broken menu button variants
    text = re.sub(r'<button class="menu-btn" onclick="toggleMenu\(\)">.*?</button>', '', text)

    # normalize nav-links id
    text = text.replace('<div class="nav-links" id="navLinks">', '<div class="nav-links">')
    text = text.replace('<div class="nav-links" id="navLinks" id="navLinks">', '<div class="nav-links">')

    # add clean button before nav-links
    text = text.replace(
        '<div class="nav-links">',
        '<button class="menu-btn" onclick="toggleMenu()">MENU</button><div class="nav-links" id="navLinks">'
    )

    # remove old css/script blocks if present
    text = re.sub(r'<style id="hamburger-menu-css">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<style id="pro-mobile-header">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="menu-script">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<script id="pro-menu-script">.*?</script>', '', text, flags=re.S)

    # insert new css/script
    text = text.replace("</head>", header_css + "\n</head>")
    text = text.replace("</body>", script + "\n</body>")

    p.write_text(text, encoding="utf-8")
    print("Fixed mobile header:", p.name)

print("Done.")
