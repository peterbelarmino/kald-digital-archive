from pathlib import Path
import re

p = Path("iso-audit.html")
html = p.read_text(encoding="utf-8", errors="ignore")

if ".converted-video" not in html:
    html = html.replace("</style>", ".converted-video{background:#d8ecff;color:#064b8a}\n.archived-master{background:#e7ddff;color:#4b238a}\n</style>", 1)
elif ".archived-master" not in html:
    html = html.replace("</style>", ".archived-master{background:#e7ddff;color:#4b238a}\n</style>", 1)

def update_status(html, cd, status, css_class):
    rows = re.findall(r"<tr\b.*?</tr>", html, flags=re.I | re.S)
    for row in rows:
        if f"<td>{cd}</td>" in row:
            new_row = re.sub(r'data-status="[^"]*"', f'data-status="{status}"', row, count=1)
            new_row = re.sub(
                r'<span class="badge [^"]*">.*?</span>',
                f'<span class="badge {css_class}">{status}</span>',
                new_row,
                count=1,
                flags=re.S
            )
            html = html.replace(row, new_row, 1)
            break
    return html

for cd in ["CD113V", "CD118V", "CD122V"]:
    html = update_status(html, cd, "Converted Video", "converted-video")

for cd in ["CD119V", "CD123V", "CD124V", "CD125V", "CD136V", "CD139"]:
    html = update_status(html, cd, "Archived Master", "archived-master")

p.write_text(html, encoding="utf-8")
print("ISO audit fixed.")
