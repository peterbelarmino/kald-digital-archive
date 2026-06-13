from pathlib import Path
import json

items=[]

# Documents
for f in Path("assets/documents").glob("*.*"):
    if f.is_file():
        items.append({
            "title":f.stem,
            "type":"Document",
            "url":f.as_posix()
        })

# Photo Galleries
for f in Path(".").glob("photos-*.html"):
    items.append({
        "title":f.stem.replace("-"," ").title(),
        "type":"Photo Gallery",
        "url":f.name
    })

# Videos
items.append({
    "title":"KALD 2019 Video Archive",
    "type":"Video",
    "url":"videos.html"
})

Path("search-data.js").write_text(
    "const archiveData = " + json.dumps(items,ensure_ascii=False,indent=2) + ";",
    encoding="utf-8"
)

print("Generated search-data.js")
print("Records:",len(items))
