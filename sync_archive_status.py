from pathlib import Path
import re

# =====================
# DASHBOARD UPDATE
# =====================
p = Path("dashboard.html")
html = p.read_text(encoding="utf-8", errors="ignore")

html = re.sub(r'<div class="card"><h2>1</h2><p>Converted Web Video</p></div>', '<div class="card"><h2>11</h2><p>Archived Master Videos</p></div>', html)
html = re.sub(r'<div class="card"><h2>11\+</h2><p>Pending Video ISOs</p></div>', '<div class="card"><h2>3</h2><p>Web Ready Videos</p></div>', html)
html = html.replace("Overall Archive Content Recovery:</b> 68%", "Overall Archive Content Recovery:</b> 74%")
html = html.replace("width:68%;background:#0b6fae", "width:74%;background:#0b6fae")
html = html.replace(">68%</div>", ">74%</div>")

p.write_text(html, encoding="utf-8")
print("dashboard.html synced")

# =====================
# ARCHIVE STATUS UPDATE
# =====================
p = Path("archive-status.html")
html = p.read_text(encoding="utf-8", errors="ignore")

html = html.replace("Approximately 68%", "Approximately 74%")
html = html.replace(
    "1 video converted for web. Many DVD/ISO video archives remain pending review and GPU conversion.",
    "11 master videos archived in Google Drive. 3 web-ready compressed videos prepared for portal use. Remaining video ISOs still pending review and conversion."
)

p.write_text(html, encoding="utf-8")
print("archive-status.html synced")

# =====================
# ISO AUDIT UPDATE
# =====================
p = Path("iso-audit.html")
html = p.read_text(encoding="utf-8", errors="ignore")

if ".archived-master" not in html:
    html = html.replace(
        ".converted-video{background:#d8ecff;color:#064b8a}",
        ".converted-video{background:#d8ecff;color:#064b8a}\n.archived-master{background:#e7ddff;color:#4b238a}"
    )

converted = ["CD113V", "CD118V", "CD122V"]
archived = ["CD119V", "CD123V", "CD124V", "CD125V", "CD136V", "CD139"]

def update_row(text, cd, status, cls):
    pattern = rf'(<tr data-status=")[^"]+(">\s*<td>{re.escape(cd)}</td>.*?<td><span class="badge )[^"]+(">) .*?(</span></td>)'
    return re.sub(pattern, rf'\1{status}\2\3{cls}\4{status}\5', text, flags=re.S)

for cd in converted:
    html = update_row(html, cd, "Converted Video", "converted-video")

for cd in archived:
    html = update_row(html, cd, "Archived Master", "archived-master")

p.write_text(html, encoding="utf-8")
print("iso-audit.html synced")
