from pathlib import Path

p = Path("videos.html")
text = p.read_text(encoding="utf-8", errors="ignore")

analytics = """
<div class="stats" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:15px;margin-bottom:25px">
<div class="card"><h2>1</h2><p>Converted Videos</p></div>
<div class="card"><h2>11</h2><p>Pending Video ISOs</p></div>
<div class="card"><h2>1</h2><p>Duplicate Videos</p></div>
<div class="card"><h2>1</h2><p>Damaged Media</p></div>
</div>
"""

if "Converted Videos</p></div>" not in text:
    text = text.replace(
        '<section class="section">',
        '<section class="section">\n' + analytics,
        1
    )

p.write_text(text, encoding="utf-8")
print("Video analytics added.")
