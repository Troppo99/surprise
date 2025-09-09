import os
from PIL import Image

# Ganti dengan lokasi folder kamu
folder_path = r"D:\video"

# Loop semua file dalam folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(folder_path, filename)
        jpg_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".jpg")

        try:
            # Buka file HEIC
            with Image.open(heic_path) as img:
                # Konversi ke RGB biar aman
                img = img.convert("RGB")
                img.save(jpg_path, "JPEG")
                print(f"Berhasil convert: {filename} → {jpg_path}")
        except Exception as e:
            print(f"Gagal convert {filename}: {e}")
