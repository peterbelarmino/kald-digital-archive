from pathlib import Path
import html

docs_dir = Path("assets/documents")
files = sorted([p for p in docs_dir.iterdir() if p.is_file()])

def doc_type(ext):
    ext = ext.lower()
    if ext in [".pdf"]: return "PDF"
    if ext in [".doc", ".docx"]: return "Word"
    if ext in [".xls", ".xlsx"]: return "Excel"
    if ext in [".ppt", ".pptx"]: return "PowerPoint"
    return "Other"

rows = []
for p in files:
    t = doc_type(p.suffix)
    size_mb = round(p.stat().st_size / 1024 / 1024, 2)
    rows.append(f"""
<tr data-type="{t}">
<td>{html.escape(p.name)}</td>
<td>{t}</td>
<td>{size_mb} MB</td>
<td><a class="btn viewbtn" href="{p.as_posix()}" target="_blank">View</a><a class="btn downloadbtn" href="{p.as_posix()}" download>Download</a></td>
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
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}}.brand img{{height:52px}}
.nav-links{{display:flex;gap:18px;margin-left:auto}}.nav-links a{{text-decoration:none;color:#0b4f8a;font-weight:700}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:55px 25px}}
.section{{max-width:1200px;margin:35px auto;padding:0 25px}}
.tools{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}}
input,select{{padding:12px;border:1px solid #ccd6e0;border-radius:10px;font-size:15px}}
input{{flex:1;min-width:250px}}
table{{width:100%;border-collapse:collapse;background:white;border-radius:16px;overflow:hidden;box-shadow:0 6px 20px #0002}}
th,td{{padding:13px;border-bottom:1px solid #e5eaf0;text-align:left;font-size:14px}}
th{{background:#0b4f8a;color:white}}
.btn{{display:inline-block;color:white;text-decoration:none;padding:8px 12px;border-radius:8px;font-weight:700}} .viewbtn{{background:#0b4f8a;margin-right:6px}} .downloadbtn{{background:#198754}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:15px;margin-bottom:22px}}
.card{{background:white;border-radius:16px;padding:18px;box-shadow:0 5px 16px #0002;border-top:5px solid #0b6fae}}
.card h2{{margin:0;color:#0b4f8a}}
footer{{text-align:center;background:#102a43;color:white;padding:25px;margin-top:45px}}
</style>
</head>
<body>
<nav><a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a><div class="nav-links"><a href="index.html">Home</a><a href="dashboard.html">Dashboard</a><a href="photos.html">Photos</a><a href="videos.html">Videos</a><a href="documents.html">Documents</a><a href="reports.html">Reports</a><a href="archive-status.html">Status</a></div></nav>

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
print(f"Generated documents.html with {len(files)} documents")

