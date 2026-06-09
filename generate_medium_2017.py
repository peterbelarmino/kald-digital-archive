from PIL import Image
from pathlib import Path

SOURCE = r"C:\Users\HP\My Drive\KALD DIGITAL ARCHIVE\Photos\2017_International_Conference"
TARGET = r"C:\Users\HP\Desktop\KALD_PORTAL\assets\medium2017"

Path(TARGET).mkdir(parents=True, exist_ok=True)

count = 0

for ext in ("*.jpg", "*.JPG", "*.jpeg", "*.JPEG", "*.png", "*.PNG"):
    for file in Path(SOURCE).rglob(ext):
        try:
            img = Image.open(file).convert("RGB")
            img.thumbnail((1600, 1200))

            out = Path(TARGET) / file.name
            img.save(out, "JPEG", optimize=True, quality=82)

            count += 1
            print("Medium:", file.name)

        except Exception as e:
            print("Error:", file.name, e)

print(f"\nFinished. {count} medium images created.")
