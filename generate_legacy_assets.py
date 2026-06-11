from PIL import Image, ImageOps
from pathlib import Path

SOURCE = r"E:\KALD PHOTOS AND VIDEOS\USB1"
THUMBS = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\thumbsLegacy"
MEDIUM = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\mediumLegacy"

Path(THUMBS).mkdir(parents=True, exist_ok=True)
Path(MEDIUM).mkdir(parents=True, exist_ok=True)

count = 0

for file in Path(SOURCE).rglob("*.*"):
    if file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue
    try:
        img = Image.open(file)
        img = ImageOps.exif_transpose(img).convert("RGB")

        safe_name = f"LEGACY_{count+1:04d}.jpg"

        thumb = img.copy()
        thumb.thumbnail((360, 260))
        thumb.save(Path(THUMBS) / safe_name, "JPEG", optimize=True, quality=74)

        medium = img.copy()
        medium.thumbnail((1200, 900))
        medium.save(Path(MEDIUM) / safe_name, "JPEG", optimize=True, quality=78)

        count += 1
        print("Processed:", safe_name)

    except Exception as e:
        print("Error:", file.name, e)

print(f"Finished. {count} Legacy photos processed.")
