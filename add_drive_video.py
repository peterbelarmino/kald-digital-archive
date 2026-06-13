from pathlib import Path

p = Path("videos.html")
text = p.read_text(encoding="utf-8", errors="ignore")

drive_link = "https://drive.google.com/file/d/1Vwbk_XBpQz4oIN35z2yhYdXDuhsQCUwl/view?usp=sharing"

video_card = '''
<div class="card" style="border-top:5px solid #0b6fae">
<h3>KALD 2019 Video Archive</h3>

<p><b>Source CD:</b> CD122V</p>
<p><b>Original Format:</b> ISO</p>
<p><b>Web Format:</b> MP4 (720p)</p>
<p><b>File Size:</b> 542 MB</p>
<p><b>Storage:</b> Google Drive</p>
<p><b>Status:</b> Converted and Available</p>

<div style="margin-top:15px">
<a class="btn" target="_blank" href="''' + drive_link + '''">View Video</a>
<a class="btn" target="_blank" href="''' + drive_link + '''">Open in Google Drive</a>
</div>

</div>
'''

if "CD122V" not in text:
    text = text.replace("</section>", video_card + "\n</section>", 1)

p.write_text(text, encoding="utf-8")
print("Video link added.")
