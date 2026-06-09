from pathlib import Path

thumb_dir = Path("assets/thumbs2017")
photos = sorted(thumb_dir.glob("*.*"))

cards = []
for photo in photos:
    name = photo.stem
    src = photo.as_posix()
    cards.append(f'''
<div class="photo">
  <img src="{src}" alt="{name}">
  <p>{name}</p>
</div>''')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>KALD 2017 International Conference Gallery</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1b2a3a}}
nav{{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a}}
.brand img{{height:52px}}
nav a{{text-decoration:none;color:#0b4f8a;font-weight:700;margin-left:18px}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:55px 25px}}
.actions{{max-width:1150px;margin:25px auto;padding:0 25px}}
.btn{{display:inline-block;background:#0b4f8a;color:white;text-decoration:none;padding:12px 18px;border-radius:10px;font-weight:700}}
.gallery{{max-width:1150px;margin:auto;padding:10px 25px 45px;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px}}
.photo{{background:white;border-radius:14px;box-shadow:0 4px 12px #0003;overflow:hidden}}
.photo img{{width:100%;height:180px;object-fit:cover;display:block}}
.photo p{{margin:0;padding:8px;text-align:center;font-size:13px;font-weight:700;color:#0b4f8a}}
footer{{text-align:center;background:#102a43;color:white;padding:25px;margin-top:35px}}
</style>
</head>
<body>
<nav><div class="brand"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></div><div><a href="index.html">Home</a><a href="dashboard.html">Dashboard</a><a href="about.html">About</a><a href="photos.html">Photos</a><a href="videos.html">Videos</a><a href="documents.html">Documents</a><a href="reports.html">Reports</a></div></nav>
<section class="hero"><h1>2017 International Conference Gallery</h1><p>{len(photos)} optimized thumbnail previews from the KALD International Conference archive.</p></section>
<div class="actions"><a class="btn" href="photos.html">Back to Photos</a></div>
<div class="gallery">
{''.join(cards)}
</div>
<footer><p>KALD Digital Archive Center | 2017 International Conference Gallery</p></footer>
</body>
</html>'''

Path("photos-2017.html").write_text(html, encoding="utf-8")
print(f"Generated photos-2017.html with {len(photos)} thumbnails.")