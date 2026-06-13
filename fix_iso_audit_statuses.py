from pathlib import Path
import re

p = Path("iso-audit.html")
text = p.read_text(encoding="utf-8", errors="ignore")

fixes = {
    "_DUPLICATES_BY_NAME": "Duplicate",
    "CD130P": "Duplicate",
    "CD71V": "Duplicate",
    "CD122V": "Converted Video",
    "CD69V_dAMAGED": "Damaged"
}

for folder, status in fixes.items():
    pattern = rf'(<tr data-status=")[^"]+(">\s*<td>{re.escape(folder)}</td>.*?<td><span class="badge )[^"]+(">) .*?(</span></td>)'
    replacement_class = status.lower().replace(" ","-").replace("/","")
    text = re.sub(
        pattern,
        rf'\1{status}\2\3{replacement_class}\4{status}\5',
        text,
        flags=re.S
    )

# add CSS for converted video badge if not exists
if ".converted-video" not in text:
    text = text.replace(
        ".recovered{background:#d9f7df;color:#0a6b1f}",
        ".recovered{background:#d9f7df;color:#0a6b1f}\n.converted-video{background:#d8ecff;color:#064b8a}"
    )

p.write_text(text, encoding="utf-8")
print("ISO Audit statuses corrected.")
