from pathlib import Path
import re

p = Path("videos.html")
text = p.read_text(encoding="utf-8", errors="ignore")

thumb_css = """
<style id="video-thumbnail-style">
.video-thumb{
  width:100%;
  max-height:210px;
  object-fit:cover;
  border-radius:14px;
  margin:12px 0;
  box-shadow:0 4px 14px #0002;
}
</style>
"""

if 'id="video-thumbnail-style"' not in text:
    text = text.replace("</head>", thumb_css + "\n</head>")

if 'assets/video-thumbnails/kald2019_cd122v.jpg' not in text:
    text = text.replace(
        '<h3>KALD 2019 Video Archive</h3>',
        '<h3>KALD 2019 Video Archive</h3>\n<img class="video-thumb" src="assets/video-thumbnails/kald2019_cd122v.jpg" alt="KALD 2019 Video Archive thumbnail">'
    )

p.write_text(text, encoding="utf-8")
print("Thumbnail added to videos.html")
