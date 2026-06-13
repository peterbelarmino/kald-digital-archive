from pathlib import Path

for p in Path(".").glob("*.html"):
    html = p.read_text(encoding="utf-8", errors="ignore")

    if 'href="video-inventory.html"' not in html:
        html = html.replace(
            '<a href="videos.html">Videos</a>',
            '<a href="videos.html">Videos</a><a href="video-inventory.html">Video Inventory</a>'
        )

    p.write_text(html, encoding="utf-8")
    print("Checked:", p.name)
