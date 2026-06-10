from PIL import Image, ImageOps
from pathlib import Path

SOURCE = r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2017_International_Conference"
THUMBS = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\thumbs2017"
MEDIUM = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\medium2017"

Path(THUMBS).mkdir(parents=True, exist_ok=True)
Path(MEDIUM).mkdir(parents=True, exist_ok=True)

count = 0

for ext in ("*.jpg", "*.JPG", "*.jpeg", "*.JPEG", "*.png", "*.PNG"):
    for file in Path(SOURCE).rglob(ext):
        try:
            img = Image.open(file)
            img = ImageOps.exif_transpose(img).convert("RGB")

            thumb = img.copy()
            thumb.thumbnail((400, 300))
            thumb.save(Path(THUMBS) / file.name, "JPEG", optimize=True, quality=80)

            medium = img.copy()
            medium.thumbnail((1600, 1200))
            medium.save(Path(MEDIUM) / file.name, "JPEG", optimize=True, quality=85)

            count += 1
            print("Fixed orientation:", file.name)

        except Exception as e:
            print("Error:", file.name, e)

print(f"Finished. Rebuilt {count} images with auto-orientation.")
