import cv2
import matplotlib.pyplot as plt

# Baca gambar dalam format RGB
image_rgb = cv2.imread(
    'c:/Users/chair/Documents/smt-5/Pengolahan Citra Digital/PASCA UTS/RGB-YCBCR/unpam.png')
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

# Konversi gambar dari RGB ke YCbCr
image_ycbcr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Pisahkan masing-masing kanal
Y, Cb, Cr = cv2.split(image_ycbcr)

# Menampilkan kanal secara individual
plt.figure(figsize=(12, 4))

# Kanal Y (luminance)
plt.subplot(1, 3, 1)
plt.imshow(Y, cmap='gray')
plt.title('Luminance (Y)')
plt.axis('off')

# Kanal Cb (chrominance-blue)
plt.subplot(1, 3, 2)
plt.imshow(Cb, cmap='gray')
plt.title('Chrominance-Blue (Cb)')
plt.axis('off')

# Kanal Cr (chrominance-red)
plt.subplot(1, 3, 3)
plt.imshow(Cr, cmap='gray')
plt.title('Chrominance-Red (Cr)')
plt.axis('off')

plt.show()
