from PIL import Image, ImageOps
from pathlib import Path

SOURCE = r"D:\KALD . 27,11,2019"
THUMBS = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\thumbs2019"
MEDIUM = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\medium2019"

Path(THUMBS).mkdir(parents=True, exist_ok=True)
Path(MEDIUM).mkdir(parents=True, exist_ok=True)

count = 0

for file in Path(SOURCE).rglob("*.*"):
    if file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue
    try:
        img = Image.open(file)
        img = ImageOps.exif_transpose(img).convert("RGB")

        safe_name = file.name.replace(" ", "_").replace("(", "").replace(")", "").replace(",", "")

        thumb = img.copy()
        thumb.thumbnail((400, 300))
        thumb.save(Path(THUMBS) / safe_name, "JPEG", optimize=True, quality=80)

        medium = img.copy()
        medium.thumbnail((1600, 1200))
        medium.save(Path(MEDIUM) / safe_name, "JPEG", optimize=True, quality=85)

        count += 1
        print("Processed:", safe_name)

    except Exception as e:
        print("Error:", file.name, e)

print(f"Finished. {count} images processed.")
