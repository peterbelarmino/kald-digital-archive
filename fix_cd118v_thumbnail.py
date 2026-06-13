from pathlib import Path
import re

path = Path("videos.html")
html = path.read_text(encoding="utf-8", errors="ignore")

# Update totals
html = re.sub(
    r'(<h2>\s*)2(\s*</h2>\s*<p>\s*Converted Videos\s*</p>)',
    r'\g<1>3\g<2>',
    html,
    count=1,
    flags=re.I
)

html = re.sub(
    r'(<h2>\s*)10(\s*</h2>\s*<p>\s*Pending Video ISOs\s*</p>)',
    r'\g<1>9\g<2>',
    html,
    count=1,
    flags=re.I
)

# Remove CD118V pending card
html = re.sub(
    r'<div class="card video-card" data-status="Pending">.*?<h3>\s*CD118V\s*/\s*VIDEO\.iso\s*</h3>.*?</div>\s*',
    '',
    html,
    count=1,
    flags=re.I | re.S
)

card = '''
<div class="card video-card" data-status="Converted">
  <span class="badge done">Converted</span>
  <h3>CD118V Video Archive</h3>

  <img class="video-thumb"
       src="assets/video-thumbnails/cd118v.jpg?v=2"
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
    html = html.replace(
        "<h2>Duplicate Videos</h2>",
        card + "<h2>Duplicate Videos</h2>",
        1
    )

path.write_text(html, encoding="utf-8")

print("CD118V card and thumbnail added to videos.html")
