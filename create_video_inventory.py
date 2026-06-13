from pathlib import Path

videos = [
("KALD 2008 Event", "KALD_2008_Event_1080p.mp4", "8.06 GB", "Archived Master"),
("KALD 2014 Event", "KALD_2014_Event_1080p.mp4", "3.35 GB", "Archived Master"),
("CD113V", "KALD_CD113V_1080p.mp4", "0.03 GB", "Archived Master"),
("CD118V", "KALD_CD118V_1080p.mp4", "9.24 GB", "Archived Master"),
("CD119V", "KALD_CD119V_1080p.mp4", "1.47 GB", "Archived Master"),
("CD122V 2019", "KALD_CD122V_2019_1080p.mp4", "4.02 GB", "Archived Master"),
("CD123V", "KALD_CD123V_1080p.mp4", "3.98 GB", "Archived Master"),
("CD124V", "KALD_CD124V_1080p.mp4", "4.21 GB", "Archived Master"),
("CD125V", "KALD_CD125V_1080p.mp4", "4.73 GB", "Archived Master"),
("CD136V", "KALD_CD136V_1080p_v2.mp4", "1.58 GB", "Archived Master"),
("CD139 2014", "KALD_CD139_2014_1080p.mp4", "7.60 GB", "Archived Master"),
]

web_ready = [
("CD113V Web 720p", "CD113V_Web_720p.mp4", "0.38 GB"),
("CD118V Web 720p", "CD118V_Web_720p.mp4", "3.51 GB"),
("CD122V Web 720p", "KALD_2019_Video_Archive_CD122V_720p.mp4", "0.53 GB"),
]

rows = ""
for title, name, size, status in videos:
    rows += f"<tr><td>{title}</td><td>{name}</td><td>{size}</td><td>{status}</td></tr>\n"

web_rows = ""
for title, name, size in web_ready:
    web_rows += f"<tr><td>{title}</td><td>{name}</td><td>{size}</td><td>Web Ready</td></tr>\n"

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>KALD Video Archive Inventory</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1b2a3a}}
nav{{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}}.brand img{{height:52px}}
.nav-links{{display:flex;gap:18px;margin-left:auto}}.nav-links a{{text-decoration:none;color:#0b4f8a;font-weight:700}}
.menu-btn{{display:none;background:#0b4f8a;color:white;border:0;border-radius:10px;padding:10px 16px;font-weight:800}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:50px 20px}}
.section{{max-width:1200px;margin:30px auto;padding:0 20px}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:15px;margin-bottom:25px}}
.card{{background:white;border-radius:18px;padding:20px;box-shadow:0 6px 20px #0002;border-top:5px solid #0b6fae}}
.card h2{{color:#0b4f8a;margin:0}}
table{{width:100%;border-collapse:collapse;background:white;border-radius:16px;overflow:hidden;box-shadow:0 6px 20px #0002;margin-bottom:28px}}
th,td{{padding:12px;border-bottom:1px solid #e5eaf0;text-align:left}}
th{{background:#0b4f8a;color:white}}
.notice{{background:#fff3cd;color:#5c4700;padding:14px;border-radius:12px;font-weight:700;margin-bottom:20px}}
footer{{text-align:center;background:#102a43;color:white;padding:25px;margin-top:45px}}
@media(max-width:768px){{nav{{padding:12px 14px!important;flex-wrap:wrap!important}}.brand img{{height:38px!important}}.brand span{{font-size:18px!important}}.menu-btn{{display:block!important}}.nav-links{{display:none!important;width:100%!important;flex-direction:column!important;gap:7px!important;margin-top:12px!important;margin-left:0!important}}.nav-links.show{{display:flex!important}}.nav-links a{{width:100%!important;text-align:center!important;background:#eef6fc!important;padding:10px!important;border-radius:10px!important}}table{{display:block;overflow-x:auto}}}}
</style>
</head>
<body>
<nav>
<a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a>
<button class="menu-btn" onclick="toggleMenu()">MENU</button>
<div class="nav-links" id="navLinks">
<a href="index.html">Home</a><a href="dashboard.html">Dashboard</a><a href="photos.html">Photos</a><a href="videos.html">Videos</a><a href="documents.html">Documents</a><a href="reports.html">Reports</a><a href="archive-status.html">Status</a><a href="iso-audit.html">Audit</a>
</div>
</nav>

<section class="hero"><h1>Video Archive Inventory</h1><p>Actual archived videos and web-ready compressed videos stored in Google Drive archive.</p></section>

<section class="section">
<div class="notice">Master video files are preserved in Google Drive archive storage. Web page playback links remain pending until official KALD shared storage is finalized.</div>

<div class="stats">
<div class="card"><h2>11</h2><p>Archived Master Videos</p></div>
<div class="card"><h2>3</h2><p>Web Ready Videos</p></div>
<div class="card"><h2>48.27 GB</h2><p>Approx. Master Video Storage</p></div>
<div class="card"><h2>4.42 GB</h2><p>Approx. Web Video Storage</p></div>
</div>

<h2>Archived Master Videos</h2>
<table><thead><tr><th>Video</th><th>File Name</th><th>Size</th><th>Status</th></tr></thead><tbody>
{rows}
</tbody></table>

<h2>Web Ready Videos</h2>
<table><thead><tr><th>Video</th><th>File Name</th><th>Size</th><th>Status</th></tr></thead><tbody>
{web_rows}
</tbody></table>
</section>

<footer><p>KALD Digital Archive Center | Video Inventory</p></footer>
<script>
function toggleMenu(){{document.getElementById("navLinks").classList.toggle("show");}}
</script>
</body>
</html>'''

Path("video-inventory.html").write_text(page, encoding="utf-8")
print("video-inventory.html created.")
