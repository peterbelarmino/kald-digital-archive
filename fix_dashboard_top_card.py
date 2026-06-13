from pathlib import Path

p = Path("dashboard.html")
html = p.read_text(encoding="utf-8")

old = '<div class="card"><h2>11</h2><p>Archived Master Videos</p></div>'

new = '<div class="card"><h2>3</h2><p>Web Ready Videos</p></div>'

html = html.replace(old, new, 1)

p.write_text(html, encoding="utf-8")

print("Dashboard top card fixed.")
