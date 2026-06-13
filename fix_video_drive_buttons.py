from pathlib import Path
import re

p = Path("videos.html")
text = p.read_text(encoding="utf-8", errors="ignore")

drive = "https://drive.google.com/file/d/1Vwbk_XBpQz4oIN35z2yhYdXDuhsQCUwl/view?usp=sharing"

new_card = f'''
<div class="card video-card" data-status="Converted">
<span class="badge done">Converted</span>
<h3>KALD 2019 Video Archive</h3>
<p><b>Source:</b> CD122V / KALD2019.iso</p>
<p><b>Duration:</b> 01:11:33</p>
<p><b>Web Size:</b> 542 MB</p>
<p><b>Format:</b> MP4 / 720p / H.264</p>
<p><b>Storage:</b> Google Drive</p>
<p><b>Status:</b> Converted and available for viewing.</p>
<div>
<a class="btn" href="{drive}" target="_blank" rel="noopener">View Video</a>
<a class="btn" href="{drive}" target="_blank" rel="noopener">Open in Google Drive</a>
</div>
</div>
'''

text = re.sub(
    r'<div class="card video-card" data-status="Converted">.*?</div>',
    new_card,
    text,
    count=1,
    flags=re.S
)

p.write_text(text, encoding="utf-8")
print("CD122V video card updated with Drive buttons.")
