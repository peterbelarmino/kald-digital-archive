from pathlib import Path
import re

css = """
<style id="backtop-fix-css">
#backTop{
  position:fixed;
  right:18px;
  bottom:18px;
  background:#0b4f8a;
  color:white;
  border:0;
  border-radius:50px;
  padding:12px 16px;
  font-weight:800;
  display:none;
  z-index:9999;
  cursor:pointer;
  box-shadow:0 4px 14px #0004;
}
</style>
"""

button = '<button id="backTop" onclick="window.scrollTo({top:0,behavior:\'smooth\'})">TOP</button>'

script = """
<script id="backtop-fix-js">
window.addEventListener("scroll",function(){
  const b=document.getElementById("backTop");
  if(b){b.style.display=window.scrollY>400?"block":"none";}
});
</script>
"""

for p in Path(".").glob("photos-*.html"):
    text=p.read_text(encoding="utf-8", errors="ignore")
    text=re.sub(r'<style id="backtop-fix-css">.*?</style>', '', text, flags=re.S)
    text=re.sub(r'<script id="backtop-fix-js">.*?</script>', '', text, flags=re.S)
    text=re.sub(r'<button id="backTop".*?</button>', '', text, flags=re.S)

    text=text.replace("</head>", css + "\n</head>")
    text=text.replace("</body>", button + "\n" + script + "\n</body>")

    p.write_text(text, encoding="utf-8")
    print("TOP restored:", p.name)

print("Done.")
