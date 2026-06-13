from pathlib import Path
import csv, html

csv_path = Path.home() / "Desktop" / "KALD_FINAL_CD_AUDIT.csv"

rows = []
with open(csv_path, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        folder = r["Folder"]
        photos = int(r["Photos"])
        docs = int(r["Docs"])
        videos = int(r["Videos"])
        iso = int(r["ISO"])

        if "DAMAGED" in folder.upper():
            status = "Damaged"
        elif folder in ["CD130P","CD71V"]:
            status = "Duplicate"
        elif photos > 0 or docs > 0 or videos > 0:
            status = "Recovered"
        elif iso > 0:
            status = "Pending ISO Review"
        else:
            status = "Empty / Review"

        rows.append((folder, photos, docs, videos, iso, status))

cards = ""
for folder, photos, docs, videos, iso, status in rows:
    cls = status.lower().replace(" ","-").replace("/","")
    cards += f"""
<tr data-status="{html.escape(status)}">
<td>{html.escape(folder)}</td>
<td>{photos}</td>
<td>{docs}</td>
<td>{videos}</td>
<td>{iso}</td>
<td><span class="badge {cls}">{html.escape(status)}</span></td>
</tr>
"""

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>KALD ISO Audit</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1b2a3a}}
nav{{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}}.brand img{{height:52px}}
.nav-links{{display:flex;gap:18px;margin-left:auto}}.nav-links a{{text-decoration:none;color:#0b4f8a;font-weight:700}}
.menu-btn{{display:none;background:#0b4f8a;color:white;border:0;border-radius:10px;padding:10px 16px;font-weight:800}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:50px 20px}}
.section{{max-width:1200px;margin:30px auto;padding:0 20px}}
.tools{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:18px}}
input,select{{padding:12px;border:1px solid #ccd6e0;border-radius:10px;font-size:15px}}
input{{flex:1;min-width:250px}}
table{{width:100%;border-collapse:collapse;background:white;border-radius:16px;overflow:hidden;box-shadow:0 6px 20px #0002}}
th,td{{padding:12px;border-bottom:1px solid #e5eaf0;text-align:left}}
th{{background:#0b4f8a;color:white}}
.badge{{padding:6px 10px;border-radius:20px;font-weight:800;font-size:12px}}
.recovered{{background:#d9f7df;color:#0a6b1f}}
.pending-iso-review{{background:#fff3cd;color:#8a5b00}}
.duplicate{{background:#e8e8e8;color:#555}}
.damaged{{background:#ffd6d6;color:#9b0000}}
.empty--review{{background:#e7f0ff;color:#0b4f8a}}
footer{{text-align:center;background:#102a43;color:white;padding:25px;margin-top:45px}}
@media(max-width:768px){{
nav{{padding:12px 14px!important;flex-wrap:wrap!important}}
.brand{{max-width:72%!important}}.brand img{{height:38px!important}}.brand span{{font-size:18px!important}}
.menu-btn{{display:block!important}}
.nav-links{{display:none!important;width:100%!important;flex-direction:column!important;gap:7px!important;margin-top:12px!important;margin-left:0!important}}
.nav-links.show{{display:flex!important}}
.nav-links a{{width:100%!important;text-align:center!important;background:#eef6fc!important;padding:10px!important;border-radius:10px!important}}
table{{display:block;overflow-x:auto}}
.hero{{padding:32px 18px!important}}
}}
</style>
</head>
<body>
<nav>
<a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a>
<button class="menu-btn" onclick="toggleMenu()">MENU</button>
<div class="nav-links" id="navLinks">
<a href="index.html">Home</a>
<a href="dashboard.html">Dashboard</a>
<a href="photos.html">Photos</a>
<a href="videos.html">Videos</a>
<a href="documents.html">Documents</a>
<a href="reports.html">Reports</a>
<a href="archive-status.html">Status</a>
</div>
</nav>

<section class="hero"><h1>ISO / CD Audit</h1><p>Complete audit of recovered folders, ISO files, photos, documents, videos, duplicates, and pending review items.</p></section>

<section class="section">
<div class="tools">
<input id="searchBox" placeholder="Search CD folder...">
<select id="statusFilter">
<option value="All">All Status</option>
<option value="Recovered">Recovered</option>
<option value="Pending ISO Review">Pending ISO Review</option>
<option value="Duplicate">Duplicate</option>
<option value="Damaged">Damaged</option>
<option value="Empty / Review">Empty / Review</option>
</select>
</div>

<table>
<thead><tr><th>Folder</th><th>Photos</th><th>Docs</th><th>Videos</th><th>ISO</th><th>Status</th></tr></thead>
<tbody id="auditTable">
{cards}
</tbody>
</table>
</section>

<footer><p>KALD Digital Archive Center | ISO Audit</p></footer>

<script>
function toggleMenu(){{document.getElementById("navLinks").classList.toggle("show");}}
const searchBox=document.getElementById("searchBox");
const statusFilter=document.getElementById("statusFilter");
const rows=[...document.querySelectorAll("#auditTable tr")];
function filterRows(){{
 const q=searchBox.value.toLowerCase();
 const s=statusFilter.value;
 rows.forEach(r=>{{
   const matchText=r.innerText.toLowerCase().includes(q);
   const matchStatus=s==="All" || r.dataset.status===s;
   r.style.display=(matchText && matchStatus)?"":"none";
 }});
}}
searchBox.addEventListener("input",filterRows);
statusFilter.addEventListener("change",filterRows);
</script>
</body>
</html>
"""

Path("iso-audit.html").write_text(page, encoding="utf-8")
print("Generated iso-audit.html:", len(rows), "records")
