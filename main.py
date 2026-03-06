import matplotlib.pyplot as plt
from PIL import Image

from watermarking import Watermarking
from metrics import psnr
import os


host_img = Image.open("host.png").convert('L')
host_img = host_img.resize((256,256))

host = [[host_img.getpixel((j,i)) for j in range(256)] for i in range(256)]


wm_img = Image.open("watermark.png").convert('L')
wm_img = wm_img.resize((256,256))

watermark = [[1 if wm_img.getpixel((j,i))>127 else 0 for j in range(256)] for i in range(256)]






wm = Watermarking() #watermakinstance

watermarked = wm.embed(host,watermark)

psnr_value = psnr(host,watermarked)
print("PSNR:",psnr_value)


tampered=[row[:] for row in watermarked]

for i in range(60,140):
    for j in range(60,140):
        tampered[i][j]=255


recovered,tamper_map = wm.extract(tampered,watermark)



fig,ax=plt.subplots(2,3,figsize=(15,10))

ax[0,0].imshow(host,cmap='gray')
ax[0,0].set_title("Original Image")

ax[0,1].imshow(watermarked,cmap='gray')
ax[0,1].set_title("Watermarked Image")

ax[0,2].imshow(tampered,cmap='gray')
ax[0,2].set_title("Tampered Image")

ax[1,0].imshow(watermark,cmap='gray')
ax[1,0].set_title("Original Watermark")

ax[1,1].imshow(recovered,cmap='gray')
ax[1,1].set_title("Extracted Watermark")

ax[1,2].imshow(tamper_map,cmap='hot')
ax[1,2].set_title("Detected Tampered Region")

for a in ax.flatten():
    a.axis("off")

plt.tight_layout()


import os

os.makedirs("results", exist_ok=True)

plt.imsave("results/original_image.png", host, cmap="gray")
plt.imsave("results/watermarked_image.png", watermarked, cmap="gray")
plt.imsave("results/tampered_image.png", tampered, cmap="gray")
plt.imsave("results/original_watermark.png", watermark, cmap="gray")
plt.imsave("results/extracted_watermark.png", recovered, cmap="gray")
plt.imsave("results/detected_tamper.png", tamper_map, cmap="hot")
plt.show()