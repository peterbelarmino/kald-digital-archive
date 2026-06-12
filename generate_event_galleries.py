from PIL import Image, ImageOps
from pathlib import Path
import html

events = [
    ("2016 Apr 13", "photos-2016-apr13.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2016\KALD_Event_13_Apr_2016_Unidentified"),
    ("2016 Sep 21", "photos-2016-sep21.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2016\KALD_Event_21_Sep_2016"),
    ("2016 Nov 01 Cultural Center", "photos-2016-nov01.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2016\Cultural_Center_Event_01_Nov_2016"),
    ("2016 Dec 03", "photos-2016-dec03.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2016\KALD_Event_03_Dec_2016"),
    ("2017 Mar 11", "photos-2017-mar11.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2017\KALD_Event_11_March_2017"),
    ("2020 Feb 15", "photos-2020-feb15.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2020\KALD_Event_15_Feb_2020"),
    ("2021 Jan 12", "photos-2021-jan12.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2021\KALD_Event_12_Jan_2021"),
    ("2021 Jan 18", "photos-2021-jan18.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2021\KALD_Event_18_Jan_2021"),
    ("2021 Jan 25", "photos-2021-jan25.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2021\KALD_Event_25_Jan_2021"),
    ("2021 Oct 09", "photos-2021-oct09.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2021\KALD_Event_09_Oct_2021"),
    ("Mrs. Amal Archive", "photos-mrs-amal.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2021\Mrs_Amal"),
    ("Conference Presentations and Formal Ceremony", "photos-conference-formal.html", r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\Unsorted_By_Event\Conference_Presentations_And_Formal_Ceremony"),
]

template_head = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><style>
body{{margin:0;font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1b2a3a}}
nav{{background:white;padding:14px 38px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 12px #0001;position:sticky;top:0;z-index:999}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;color:#0b4f8a;text-decoration:none}}.brand img{{height:52px}}
.nav-links{{display:flex;gap:18px;margin-left:auto}}.nav-links a{{text-decoration:none;color:#0b4f8a;font-weight:700}}
.hero{{background:linear-gradient(135deg,#083d6b,#0b6fae);color:white;text-align:center;padding:45px 25px}}
.actions,.gallery{{max-width:1150px;margin:auto;padding:20px}}
.btn{{display:inline-block;background:#0b4f8a;color:white;text-decoration:none;padding:10px 14px;border-radius:10px;font-weight:700}}
.gallery{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}}
.photo{{background:white;border-radius:14px;box-shadow:0 4px 12px #0002;overflow:hidden;text-align:center}}
.photo img{{width:100%;height:145px;object-fit:cover;display:block}}
.photo p{{font-size:12px;font-weight:700;color:#0b4f8a;padding:7px;margin:0}}
footer{{text-align:center;background:#102a43;color:white;padding:22px;margin-top:35px}}
</style></head><body>
<nav><a class="brand" href="index.html"><img src="assets/logo.jpg"><span>KALD Digital Archive</span></a><div class="nav-links"><a href="index.html">Home</a><a href="dashboard.html">Dashboard</a><a href="photos.html">Photos</a><a href="videos.html">Videos</a><a href="documents.html">Documents</a><a href="reports.html">Reports</a></div></nav>
<section class="hero"><h1>{title}</h1><p>{count} recovered photos</p></section><div class="actions"><a class="btn" href="photos.html">Back to Photos</a></div><section class="gallery">
"""

for title, page, source in events:
    src = Path(source)
    slug = page.replace(".html","")
    thumb_dir = Path("assets") / "event_galleries" / slug / "thumbs"
    medium_dir = Path("assets") / "event_galleries" / slug / "medium"
    thumb_dir.mkdir(parents=True, exist_ok=True)
    medium_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in src.rglob("*") if p.suffix.lower() in [".jpg",".jpeg",".png"]])
    cards = []

    for i, file in enumerate(files, 1):
        safe = f"{slug}_{i:04d}.jpg"
        try:
            img = Image.open(file)
            img = ImageOps.exif_transpose(img).convert("RGB")

            t = img.copy()
            t.thumbnail((360,260))
            t.save(thumb_dir / safe, "JPEG", optimize=True, quality=74)

            m = img.copy()
            m.thumbnail((1200,900))
            m.save(medium_dir / safe, "JPEG", optimize=True, quality=78)

            cards.append(f'<div class="photo"><a target="_blank" href="{(medium_dir/safe).as_posix()}"><img loading="lazy" src="{(thumb_dir/safe).as_posix()}"></a><p>{html.escape(file.stem)}</p></div>')
        except Exception as e:
            print("ERROR", file, e)

    page_html = template_head.format(title=html.escape(title), count=len(cards)) + "\n".join(cards) + "</section><footer><p>KALD Digital Archive Center</p></footer></body></html>"
    Path(page).write_text(page_html, encoding="utf-8")
    print(f"Generated {page}: {len(cards)} photos")
