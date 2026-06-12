from pathlib import Path
import re
import urllib.parse

p = Path("documents.html")
text = p.read_text(encoding="utf-8", errors="ignore")

base = "https://peterbelarmino.github.io/kald-digital-archive/"

def replace_action(match):
    file_path = match.group(1)
    file_url = base + file_path.replace(" ", "%20")
    viewer_url = "https://docs.google.com/gview?embedded=true&url=" + urllib.parse.quote(file_url, safe="")
    return f'<td><a class="btn" href="{viewer_url}" target="_blank" rel="noopener">View</a> <a class="btn" href="{file_path}" download>Download</a></td>'

text = re.sub(
    r'<td><a class="btn" href="([^"]+)" target="_blank" rel="noopener">View</a>\s*<a class="btn" href="\1" download>Download</a></td>',
    replace_action,
    text
)

p.write_text(text, encoding="utf-8")
print("Updated View buttons to Google Docs Viewer preview.")
