from pathlib import Path
import re

# Update videos.html
p = Path("videos.html")
text = p.read_text(encoding="utf-8", errors="ignore")

# analytics count
text = text.replace('<div class="card"><h2>1</h2><p>Converted Videos</p></div>', '<div class="card"><h2>2</h2><p>Converted Videos</p></div>')
text = text.replace('<div class="card"><h2>11</h2><p>Pending Video ISOs</p></div>', '<div class="card"><h2>10</h2><p>Pending Video ISOs</p></div>')

cd113v_card = '''
<div class="card video-card" data-status="Converted">
<span class="badge done">Converted</span>
<h3>CD113V Video Archive</h3>
<img class="video-thumb" src="assets/video-thumbnails/cd113v.jpg" alt="CD113V Video Archive thumbnail">
<p><b>Source:</b> CD113V / PP_DVD2_NTSC.iso</p>
<p><b>Duration:</b> 00:14:59</p>
<p><b>Web Size:</b> 391.51 MB</p>
<p><b>Format:</b> MP4 / 720p / H.264</p>
<p><b>Storage:</b> Google Drive master archive / Web compressed folder</p>
<p><b>Status:</b> Converted and ready for final storage link.</p>
<p><b>Video Link:</b> Pending public/shared-drive setup</p>
</div>
'''

if "CD113V Video Archive" not in text:
    text = text.replace('<h2>Duplicate Videos</h2>', cd113v_card + '\n\n<h2>Duplicate Videos</h2>')

# remove CD113V from pending list
text = re.sub(
    r'<div class="card video-card" data-status="Pending"><span class="badge pending">Pending</span><h3>CD113V / PP_DVD2_NTSC\.iso</h3><p>Size: 4\.11 GB</p></div>\s*',
    '',
    text
)

p.write_text(text, encoding="utf-8")
print("videos.html updated: CD113V converted.")

# Update iso-audit.html
p = Path("iso-audit.html")
text = p.read_text(encoding="utf-8", errors="ignore")

# Add converted-video css if missing
if ".converted-video" not in text:
    text = text.replace(
        ".recovered{background:#d9f7df;color:#0a6b1f}",
        ".recovered{background:#d9f7df;color:#0a6b1f}\n.converted-video{background:#d8ecff;color:#064b8a}"
    )

pattern = r'(<tr data-status=")[^"]+(">\s*<td>CD113V</td>.*?<td><span class="badge )[^"]+(">) .*?(</span></td>)'
text = re.sub(
    pattern,
    r'\1Converted Video\2\3converted-video\4Converted Video\5',
    text,
    flags=re.S
)

p.write_text(text, encoding="utf-8")
print("iso-audit.html updated: CD113V Converted Video.")
