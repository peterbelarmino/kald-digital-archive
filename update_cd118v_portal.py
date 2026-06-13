from pathlib import Path
import re
import sys

def read_file(path):
    if not path.exists():
        print(f"ERROR: Missing file: {path}")
        sys.exit(1)
    return path.read_text(encoding="utf-8", errors="ignore")

# =========================================================
# VIDEOS PAGE
# =========================================================
videos_path = Path("videos.html")
html = read_file(videos_path)

# Update statistics
html, converted_count = re.subn(
    r'(<h2>\s*)2(\s*</h2>\s*<p>\s*Converted Videos\s*</p>)',
    r'\g<1>3\g<2>',
    html,
    count=1,
    flags=re.I
)

html, pending_count = re.subn(
    r'(<h2>\s*)10(\s*</h2>\s*<p>\s*Pending Video ISOs\s*</p>)',
    r'\g<1>9\g<2>',
    html,
    count=1,
    flags=re.I
)

# Remove CD118V pending card
pending_pattern = r'''
<div\s+class=["']card\s+video-card["']\s+data-status=["']Pending["']>
.*?
<h3>\s*CD118V\s*/\s*VIDEO\.iso\s*</h3>
.*?
</div>\s*
'''

html, removed_count = re.subn(
    pending_pattern,
    "",
    html,
    count=1,
    flags=re.I | re.S | re.X
)

# Add converted card
cd118_card = '''
<div class="card video-card" data-status="Converted">
  <span class="badge done">Converted</span>
  <h3>CD118V Video Archive</h3>
  <img class="video-thumb"
       src="assets/video-thumbnails/cd118v.jpg"
       alt="CD118V Video Archive thumbnail">
  <p><b>Source:</b> CD118V / VIDEO.iso</p>
  <p><b>Duration:</b> 01:48:04</p>
  <p><b>Web Size:</b> 3.51 GB</p>
  <p><b>Format:</b> MP4 / 720p / H.264</p>
  <p><b>Storage:</b> Google Drive master archive / Web_Compressed</p>
  <p><b>Status:</b> Converted, enhanced, verified, and preserved.</p>
  <p><b>Video Link:</b> Pending authorized shared-drive setup</p>
</div>

'''

if "CD118V Video Archive" not in html:
    marker = "<h2>Duplicate Videos</h2>"

    if marker not in html:
        print("ERROR: Duplicate Videos heading was not found.")
        sys.exit(1)

    html = html.replace(marker, cd118_card + marker, 1)
    inserted_count = 1
else:
    inserted_count = 0

videos_path.write_text(html, encoding="utf-8")

print("videos.html:")
print(f"  Converted count updated: {converted_count}")
print(f"  Pending count updated:   {pending_count}")
print(f"  Pending card removed:    {removed_count}")
print(f"  Converted card inserted: {inserted_count}")

# =========================================================
# ISO AUDIT PAGE
# =========================================================
audit_path = Path("iso-audit.html")
audit = read_file(audit_path)

if ".converted-video" not in audit:
    audit = audit.replace(
        "</style>",
        """
.converted-video {
  background: #d8ecff;
  color: #064b8a;
}
</style>
""",
        1
    )

rows = re.findall(r"<tr\b.*?</tr>", audit, flags=re.I | re.S)
updated_row = False

for old_row in rows:
    if re.search(r"\bCD118V\b", old_row, flags=re.I):
        new_row = old_row

        new_row = re.sub(
            r'data-status=["'][^"']*["']',
            'data-status="Converted Video"',
            new_row,
            count=1,
            flags=re.I
        )

        new_row = re.sub(
            r'<span\s+class=["']badge[^"']*["']>.*?</span>',
            '<span class="badge converted-video">Converted Video</span>',
            new_row,
            count=1,
            flags=re.I | re.S
        )

        new_row = new_row.replace("Pending ISO Review", "Converted Video")

        audit = audit.replace(old_row, new_row, 1)
        updated_row = True
        break

audit_path.write_text(audit, encoding="utf-8")

print("iso-audit.html:")
print(f"  CD118V row updated: {updated_row}")

if converted_count == 0 or pending_count == 0 or not updated_row:
    print("\nWARNING: May bahagi ng page na hindi tumugma. Huwag munang mag-commit.")
else:
    print("\nSUCCESS: CD118V portal update completed.")
