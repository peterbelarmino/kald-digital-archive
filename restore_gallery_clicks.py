from pathlib import Path
import re

pages = [
"photos-2016-apr13.html",
"photos-2016-sep21.html",
"photos-2016-nov01.html",
"photos-2016-dec03.html",
"photos-2017-mar11.html",
"photos-2020-feb15.html",
"photos-2021-jan12.html",
"photos-2021-jan18.html",
"photos-2021-jan25.html",
"photos-2021-oct09.html",
"photos-mrs-amal.html",
"photos-conference-formal.html",
"photos-2017.html",
"photos-2019.html",
"photos-legacy.html"
]

for page in pages:
    p = Path(page)
    if not p.exists():
        continue

    text = p.read_text(encoding="utf-8", errors="ignore")

    # remove broken pro viewer scripts/styles
    text = re.sub(r'<style id="photo-viewer-pro-css">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="photo-viewer-pro-js">.*?</script>', '', text, flags=re.S)
    text = re.sub(r'<div class="viewer" id="viewer">.*?</div>\s*<button id="backTop".*?</button>', '', text, flags=re.S)

    # ensure photo links open in new tab
    text = re.sub(r'<a href="([^"]+)">', r'<a href="\1" target="_blank" rel="noopener">', text)

    p.write_text(text, encoding="utf-8")
    print("Restored clickable photos:", page)

print("Done restoring gallery click behavior.")
