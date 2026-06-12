from pathlib import Path
import re

p = Path("documents.html")
text = p.read_text(encoding="utf-8", errors="ignore")

def fix_row(match):
    filename = match.group(1)
    filetype = match.group(2)
    size = match.group(3)
    old_action = match.group(4)

    href = re.search(r'href="([^"]+)"', old_action)
    if not href:
        return match.group(0)

    path = href.group(1)

    if filetype == "PDF":
        action = f'<a class="btn" href="{path}" target="_blank" rel="noopener">View</a> <a class="btn" href="{path}" download>Download</a>'
    else:
        action = f'<span style="color:#777;font-weight:700">Preview not available</span> <a class="btn" href="{path}" download>Download</a>'

    return f"<tr data-type=\"{filetype}\">\n<td>{filename}</td>\n<td>{filetype}</td>\n<td>{size}</td>\n<td>{action}</td>\n</tr>"

text = re.sub(
    r'<tr data-type="([^"]+)">\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>',
    lambda m: fix_row((lambda x: type("M",(object,),{"group":lambda self,i: [None,x.group(2),x.group(3),x.group(4),x.group(5)][i]})())(m)),
    text,
    flags=re.S
)

p.write_text(text, encoding="utf-8")
print("Fixed documents: PDF view only, Office files download only.")
