from PIL import Image, ImageOps
from pathlib import Path

folders = [
    r"C:\Users\HP\Desktop\KALD_PORTAL\assets\thumbs2017",
    r"C:\Users\HP\Desktop\KALD_PORTAL\assets\medium2017"
]

fixed = 0

for folder in folders:
    for file in Path(folder).glob("*.*"):
        try:
            img = Image.open(file)
            img = ImageOps.exif_transpose(img).convert("RGB")
            img.save(file, "JPEG", optimize=True, quality=85)
            fixed += 1
            print("Fixed:", file.name)
        except Exception as e:
            print("Error:", file.name, e)

print(f"Finished. Fixed {fixed} images.")
