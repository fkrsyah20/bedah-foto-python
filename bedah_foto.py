from PIL import Image, ExifTags
import numpy as np
import matplotlib.pyplot as plt
import os


# ==================================================
# 1. MEMBUKA GAMBAR
# ==================================================

foto = "gambar.jpg.jpeg"
img = Image.open(foto)


# ==================================================
# 2. INFORMASI FILE
# ==================================================

print("\n=== INFORMASI FILE GAMBAR ===")

file_size = os.path.getsize(foto)

print("Nama file   :", os.path.basename(foto))
print("Ukuran file :", file_size, "byte")
print("Format      :", img.format)
print("Dimensi     :", img.size)
print("Mode        :", img.mode)


# ==================================================
# 3. DATA PIXEL
# ==================================================

pixels = np.array(img.convert("RGB"))

print("\n=== DATA PIXEL ===")
print("Shape          :", pixels.shape)
print("Tipe data      :", pixels.dtype)
print("Nilai minimum  :", pixels.min())
print("Nilai maksimum :", pixels.max())


# ==================================================
# 4. JUMLAH DATA GAMBAR
# ==================================================

print("\n=== JUMLAH DATA GAMBAR ===")

height, width = pixels.shape[:2]

total_pixels = height * width
total_angka = pixels.size

print("Tinggi gambar  :", height)
print("Lebar gambar   :", width)
print("Total pixel    :", total_pixels)
print("Total angka RGB:", total_angka)


# ==================================================
# 5. CONTOH ANGKA PIXEL
# ==================================================

print("\n=== CONTOH ANGKA PIXEL ===")

print(pixels[:5, :5, :])


# ==================================================
# 6. METADATA EXIF
# ==================================================

print("\n=== METADATA EXIF ===")

exif = img.getexif()

if len(exif) == 0:
    print("Tidak ada data EXIF yang terbaca.")
else:
    for tag_id, value in exif.items():
        tag_name = ExifTags.TAGS.get(tag_id, tag_id)
        print(tag_name, ":", value)


# ==================================================
# 7. SISTEM KOORDINAT
# ==================================================

print("\n=== SISTEM KOORDINAT GAMBAR ===")

print("X minimum :", 0)
print("X maksimum :", width - 1)

print("Y minimum :", 0)
print("Y maksimum :", height - 1)

print("\nUkuran matriks pixel:")
print("Y =", height)
print("X =", width)


# ==================================================
# 8. PIXEL TENGAH
# ==================================================

print("\n=== ANALISIS PIXEL TENGAH ===")

x = width // 2
y = height // 2

r, g, b = pixels[y, x]

print("Koordinat X :", x)
print("Koordinat Y :", y)
print("Red         :", r)
print("Green       :", g)
print("Blue        :", b)


# ==================================================
# 9. DATA KOORDINAT DAN RGB
# ==================================================

print("\n=== DATA KOORDINAT DAN RGB ===")

for y_data in range(5):
    for x_data in range(5):

        r, g, b = pixels[y_data, x_data]

        print(
            "X =", x_data,
            "Y =", y_data,
            "RGB =", [r, g, b]
        )


# ==================================================
# 10. CHANNEL RGB
# ==================================================

print("\n=== CHANNEL RGB ===")

red = pixels[:, :, 0]
green = pixels[:, :, 1]
blue = pixels[:, :, 2]

print("Ukuran channel Red   :", red.shape)
print("Ukuran channel Green :", green.shape)
print("Ukuran channel Blue  :", blue.shape)


# ==================================================
# 11. STATISTIK RGB
# ==================================================

print("\n=== STATISTIK RGB ===")

print("RED")
print("Minimum          :", red.min())
print("Maximum          :", red.max())
print("Rata-rata        :", red.mean())
print("Standar deviasi  :", red.std())

print("\nGREEN")
print("Minimum          :", green.min())
print("Maximum          :", green.max())
print("Rata-rata        :", green.mean())
print("Standar deviasi  :", green.std())

print("\nBLUE")
print("Minimum          :", blue.min())
print("Maximum          :", blue.max())
print("Rata-rata        :", blue.mean())
print("Standar deviasi  :", blue.std())


# ==================================================
# 12. PERBANDINGAN RGB
# ==================================================

print("\n=== PERBANDINGAN RGB ===")

print("Red   :", red.mean(), "±", red.std())
print("Green :", green.mean(), "±", green.std())
print("Blue  :", blue.mean(), "±", blue.std())


# ==================================================
# 13. VISUALISASI KOORDINAT X DAN Y
# ==================================================

plt.figure(figsize=(8, 6))

plt.imshow(img)

plt.xlabel("Sumbu X (Pixel)")
plt.ylabel("Sumbu Y (Pixel)")
plt.title("Koordinat X dan Y pada Citra")

plt.show()


# ==================================================
# 14. VISUALISASI CHANNEL RGB
# ==================================================

plt.figure(figsize=(6, 5))
plt.imshow(red, cmap="Reds")
plt.title("Channel Red")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


plt.figure(figsize=(6, 5))
plt.imshow(green, cmap="Greens")
plt.title("Channel Green")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


plt.figure(figsize=(6, 5))
plt.imshow(blue, cmap="Blues")
plt.title("Channel Blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# ==================================================
# 15. HISTOGRAM RGB
# ==================================================

print("\n=== HISTOGRAM RGB ===")

plt.figure(figsize=(10, 5))

plt.hist(red.ravel(), bins=256, alpha=0.5, label="Red")
plt.hist(green.ravel(), bins=256, alpha=0.5, label="Green")
plt.hist(blue.ravel(), bins=256, alpha=0.5, label="Blue")

plt.xlabel("Nilai Intensitas (0-255)")
plt.ylabel("Jumlah Pixel")
plt.title("Histogram RGB")
plt.legend()

plt.show()


# ==================================================
# 16. MENYIMPAN DATA PIXEL
# ==================================================

print("\n=== MENYIMPAN DATA PIXEL ===")

np.save("pixel_data.npy", pixels)

print("Data pixel berhasil disimpan.")
print("Nama file: pixel_data.npy")


# ==================================================
# 17. MEMBACA KEMBALI DATA PIXEL
# ==================================================

print("\n=== MEMBACA KEMBALI DATA PIXEL ===")

data = np.load("pixel_data.npy")

print("Shape data :", data.shape)
print("Tipe data  :", data.dtype)
print("Pixel tengah :", data[y, x])


# ==================================================
# 18. REKONSTRUKSI GAMBAR
# ==================================================

print("\n=== REKONSTRUKSI GAMBAR ===")

plt.figure(figsize=(8, 6))

plt.imshow(data)

plt.title("Gambar dari Data Pixel")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()


# ==================================================
# 19. METADATA DETAIL
# ==================================================

print("\n=== METADATA DETAIL ===")

print("Lebar        :", img.width, "pixel")
print("Tinggi       :", img.height, "pixel")
print("Jumlah pixel :", img.width * img.height)
print("Channel      :", len(img.getbands()))
print("Nama channel :", img.getbands())