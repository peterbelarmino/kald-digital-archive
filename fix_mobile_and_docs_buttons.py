from pathlib import Path
import re

pages = list(Path(".").glob("*.html"))

menu_script = """
<script id="menu-script">
function toggleMenu(){
  const nav = document.getElementById("navLinks");
  if(nav){ nav.classList.toggle("show"); }
}
</script>
"""

menu_css = """
<style id="hamburger-menu-css">
.menu-btn{display:none;background:#0b4f8a;color:white;border:0;border-radius:10px;padding:10px 14px;font-weight:800;cursor:pointer}
@media(max-width:768px){
  .menu-btn{display:block!important;width:100%;margin-top:8px}
  .nav-links{display:none!important;width:100%!important;flex-direction:column!important;margin-left:0!important}
  .nav-links.show{display:flex!important}
  .nav-links a{width:100%!important;box-sizing:border-box!important;text-align:center!important}
}
</style>
"""

for p in pages:
    text = p.read_text(encoding="utf-8", errors="ignore")

    # Add hamburger button and navLinks id if normal nav exists
    if '<div class="nav-links">' in text and 'class="menu-btn"' not in text:
        text = text.replace(
            '<div class="nav-links">',
            '<button class="menu-btn" onclick="toggleMenu()">? Menu</button><div class="nav-links" id="navLinks">'
        )

    # If nav-links already exists but no id
    text = text.replace('<div class="nav-links" id="navLinks" id="navLinks">', '<div class="nav-links" id="navLinks">')

    if 'id="hamburger-menu-css"' not in text:
        text = text.replace("</head>", menu_css + "\n</head>")

    if 'id="menu-script"' not in text:
        text = text.replace("</body>", menu_script + "\n</body>")

    p.write_text(text, encoding="utf-8")
    print("Updated mobile menu:", p.name)

# Fix documents View / Download buttons
doc = Path("documents.html")
text = doc.read_text(encoding="utf-8", errors="ignore")

text = re.sub(
    r'<td><a class="btn" href="([^"]+)" target="_blank">(?:Open / Download|View File|Open)</a></td>',
    r'<td><a class="btn" href="\1" target="_blank" rel="noopener">View</a> <a class="btn" href="\1" download>Download</a></td>',
    text
)

doc.write_text(text, encoding="utf-8")
print("Separated View and Download buttons in documents.html")
