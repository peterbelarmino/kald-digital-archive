from pathlib import Path
import re

css = """
<style id="final-mobile-polish">
@media(max-width:768px){
  nav{
    padding:12px 14px!important;
    display:flex!important;
    flex-direction:row!important;
    align-items:center!important;
    justify-content:space-between!important;
    flex-wrap:wrap!important;
  }
  .brand{
    max-width:72%!important;
    gap:8px!important;
    font-size:14px!important;
    line-height:1.1!important;
  }
  .brand img{
    height:38px!important;
  }
  .brand span{
    white-space:normal!important;
    font-size:18px!important;
  }
  .menu-btn{
    display:block!important;
    margin:0!important;
    padding:10px 16px!important;
    border-radius:12px!important;
    background:#0b4f8a!important;
    color:white!important;
    font-weight:800!important;
    border:0!important;
  }
  .nav-links{
    display:none!important;
    width:100%!important;
    flex-direction:column!important;
    gap:7px!important;
    margin-top:12px!important;
    margin-left:0!important;
  }
  .nav-links.show{
    display:flex!important;
  }
  .nav-links a{
    width:100%!important;
    padding:9px!important;
    text-align:center!important;
    border-radius:10px!important;
    background:#eef6fc!important;
    box-sizing:border-box!important;
    font-size:14px!important;
  }
  .hero{
    padding:32px 18px!important;
  }
  .hero h1{
    font-size:32px!important;
    line-height:1.15!important;
  }
  .hero p{
    font-size:17px!important;
    line-height:1.35!important;
  }
}
</style>
"""

script = """
<script id="final-mobile-menu-script">
function toggleMenu(){
  const nav=document.getElementById("navLinks");
  if(nav){nav.classList.toggle("show");}
}
</script>
"""

for p in Path(".").glob("*.html"):
    text = p.read_text(encoding="utf-8", errors="ignore")

    text = re.sub(r'<style id="final-mobile-polish">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="final-mobile-menu-script">.*?</script>', '', text, flags=re.S)

    text = re.sub(r'<button class="menu-btn" onclick="toggleMenu\(\)">.*?</button>', '', text)
    text = text.replace('<div class="nav-links" id="navLinks">', '<div class="nav-links">')

    text = text.replace(
        '<div class="nav-links">',
        '<button class="menu-btn" onclick="toggleMenu()">MENU</button><div class="nav-links" id="navLinks">'
    )

    text = text.replace('</head>', css + '\n</head>')
    text = text.replace('</body>', script + '\n</body>')

    p.write_text(text, encoding="utf-8")
    print("Polished:", p.name)

print("Done mobile polish.")
