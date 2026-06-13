from pathlib import Path
import html, urllib.parse

docs_dir = Path("assets/documents")
files = sorted([p for p in docs_dir.iterdir() if p.is_file() and p.name.lower() != "desktop.ini"])

base = "https://peterbelarmino.github.io/kald-digital-archive/"

def doc_type(ext):
    ext = ext.lower()
    if ext == ".pdf": return "PDF"
    if ext in [".doc", ".docx"]: return "Word"
    if ext in [".xls", ".xlsx"]: return "Excel"
    if ext in [".ppt", ".pptx"]: return "PowerPoint"
    return "Other"

rows = []
for p in files:
    t = doc_type(p.suffix)
    size_mb = round(p.stat().st_size / 1024 / 1024, 2)
    file_path = p.as_posix()
    file_url = base + urllib.parse.quote(file_path, safe="/:")

    if t == "PDF":
        view_url = file_path
        view_label = "View PDF"
    elif t in ["Word", "Excel", "PowerPoint"]:
        view_url = "https://view.officeapps.live.com/op/embed.aspx?src=" + urllib.parse.quote(file_url, safe="")
        view_label = "View"
    else:
        view_url = file_path
        view_label = "View"

    rows.append(f"""
<tr data-type="{t}">
<td>{html.escape(p.name)}</td>
<td>{t}</td>
<td>{size_mb} MB</td>
<td class="actions-cell">
<a class="doc-btn view-btn" href="{view_url}" target="_blank" rel="noopener">View</a>
<a class="doc-btn download-btn" href="{file_path}" download>Download</a>
</td>
</tr>
""")

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>KALD Document Archive</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1b2a3a}}
nav{{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}}
.brand img{{height:52px}}
.nav-links{{display:flex;gap:18px;margin-left:auto}}
.nav-links a{{text-decoration:none;color:#0b4f8a;font-weight:700}}
.menu-btn{{display:none;background:#0b4f8a;color:white;border:0;border-radius:10px;padding:10px 16px;font-weight:800;cursor:pointer}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:55px 25px}}
.section{{max-width:1200px;margin:35px auto;padding:0 25px}}
.tools{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}}
input,select{{padding:12px;border:1px solid #ccd6e0;border-radius:10px;font-size:15px}}
input{{flex:1;min-width:250px}}
table{{width:100%;border-collapse:collapse;background:white;border-radius:16px;overflow:hidden;box-shadow:0 6px 20px #0002}}
th,td{{padding:13px;border-bottom:1px solid #e5eaf0;text-align:left;font-size:14px}}
th{{background:#0b4f8a;color:white}}
.doc-btn{{display:inline-block;background:#0b4f8a!important;color:#fff!important;text-decoration:none!important;padding:10px 14px;border-radius:10px;font-weight:800;text-align:center;margin:3px}}
.download-btn{{background:#083d6b!important}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:15px;margin-bottom:22px}}
.card{{background:white;border-radius:16px;padding:18px;box-shadow:0 5px 16px #0002;border-top:5px solid #0b6fae}}
.card h2{{margin:0;color:#0b4f8a}}
footer{{text-align:center;background:#102a43;color:white;padding:25px;margin-top:45px}}

@media(max-width:768px){{
  nav{{padding:12px 14px!important;flex-direction:row!important;align-items:center!important;justify-content:space-between!important;flex-wrap:wrap!important}}
  .brand{{max-width:72%!important;font-size:14px!important;line-height:1.1!important}}
  .brand img{{height:38px!important}}
  .brand span{{font-size:18px!important}}
  .menu-btn{{display:block!important}}
  .nav-links{{display:none!important;width:100%!important;flex-direction:column!important;gap:7px!important;margin-top:12px!important;margin-left:0!important}}
  .nav-links.show{{display:flex!important}}
  .nav-links a{{width:100%!important;box-sizing:border-box!important;text-align:center!important;background:#eef6fc!important;color:#0b4f8a!important;padding:10px!important;border-radius:10px!important;font-size:14px!important}}
  .hero{{padding:32px 18px!important}}
  .hero h1{{font-size:32px!important;line-height:1.15!important}}
  .hero p{{font-size:17px!important;line-height:1.35!important}}
  .section{{padding:14px!important;margin:18px auto!important}}
  .stats{{grid-template-columns:1fr 1fr!important;gap:10px!important}}
  .card{{padding:14px!important}}
  .card h2{{font-size:28px!important}}
  table,thead,tbody,th,td,tr{{display:block!important}}
  thead{{display:none!important}}
  table{{box-shadow:none!important;background:transparent!important;white-space:normal!important;overflow:visible!important}}
  tbody tr{{background:white!important;margin:12px 0!important;padding:14px!important;border-radius:16px!important;box-shadow:0 5px 14px #0002!important}}
  tbody td{{border:0!important;padding:6px 0!important;white-space:normal!important;word-break:break-word!important;font-size:14px!important}}
  tbody td:nth-child(1){{font-weight:800!important;color:#0b4f8a!important;font-size:15px!important}}
  tbody td:nth-child(2)::before{{content:"Type: ";font-weight:800;color:#526173}}
  tbody td:nth-child(3)::before{{content:"Size: ";font-weight:800;color:#526173}}
  .actions-cell{{background:#f1f7fc!important;padding:12px!important;border-radius:12px!important;margin-top:8px!important}}
  .actions-cell::before{{content:"Action";display:block;font-weight:900;color:#0b4f8a;margin-bottom:8px}}
  .actions-cell .doc-btn{{display:block!important;width:100%!important;box-sizing:border-box!important;margin:8px 0!important;padding:13px!important;font-size:15px!important;background:#0b4f8a!important;color:#fff!important;opacity:1!important;visibility:visible!important}}
  .actions-cell .download-btn{{background:#083d6b!important}}
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

<section class="hero"><h1>Document Archive</h1><p>Recovered PDF, Word, Excel, and PowerPoint documents.</p></section>

<section class="section">
<div class="stats">
<div class="card"><h2>{len(files)}</h2><p>Total Documents</p></div>
<div class="card"><h2>{sum(1 for p in files if doc_type(p.suffix)=='PDF')}</h2><p>PDF Files</p></div>
<div class="card"><h2>{sum(1 for p in files if doc_type(p.suffix)=='Word')}</h2><p>Word Files</p></div>
<div class="card"><h2>{sum(1 for p in files if doc_type(p.suffix)=='Excel')}</h2><p>Excel Files</p></div>
<div class="card"><h2>{sum(1 for p in files if doc_type(p.suffix)=='PowerPoint')}</h2><p>PowerPoint Files</p></div>
</div>

<div class="tools">
<input id="searchBox" placeholder="Search document name...">
<select id="typeFilter">
<option value="All">All Types</option>
<option value="PDF">PDF</option>
<option value="Word">Word</option>
<option value="Excel">Excel</option>
<option value="PowerPoint">PowerPoint</option>
</select>
</div>

<table>
<thead><tr><th>Document Name</th><th>Type</th><th>Size</th><th>Action</th></tr></thead>
<tbody id="docTable">
{''.join(rows)}
</tbody>
</table>
</section>

<footer><p>KALD Digital Archive Center | Documents</p></footer>

<script>
function toggleMenu(){{
  const nav=document.getElementById("navLinks");
  if(nav){{nav.classList.toggle("show");}}
}}

const searchBox=document.getElementById('searchBox');
const typeFilter=document.getElementById('typeFilter');
const rows=[...document.querySelectorAll('#docTable tr')];

function filterDocs(){{
 const q=searchBox.value.toLowerCase();
 const type=typeFilter.value;
 rows.forEach(r=>{{
   const name=r.children[0].innerText.toLowerCase();
   const rtype=r.dataset.type;
   const show=name.includes(q) && (type==='All' || rtype===type);
   r.style.display=show?'':'none';
 }});
}}
searchBox.addEventListener('input',filterDocs);
typeFilter.addEventListener('change',filterDocs);
</script>
</body>
</html>
"""

Path("documents.html").write_text(page, encoding="utf-8")
print(f"Permanent fixed documents.html with {len(files)} documents")
