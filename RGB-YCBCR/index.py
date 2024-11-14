import cv2
import matplotlib.pyplot as plt

# Baca gambar dalam format RGB
# Ganti dengan path gambar yang ingin Anda gunakan
image_rgb = cv2.imread(
    'c:/Users/chair/Documents/smt-5/Pengolahan Citra Digital/PASCA UTS/RGB-YCBCR/unpam.png')
# OpenCV baca dalam BGR, ubah ke RGB
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

# Konversi gambar dari RGB ke YCbCr
image_ycbcr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Menampilkan gambar asli dan hasil konversi
plt.figure(figsize=(10, 5))

# Gambar asli (RGB)
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Gambar Asli (RGB)')
plt.axis('off')

# Gambar hasil konversi (YCbCr)
plt.subplot(1, 2, 2)
plt.imshow(image_ycbcr)
plt.title('Gambar Hasil Konversi (YCbCr)')
plt.axis('off')

plt.show()
