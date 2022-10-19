# tugas 1 show rgb image
from PIL import Image
import cv2
import matplotlib.pyplot as plt

file_name = "mario.jpg"

img = Image.open(file_name)

img = img.resize((5, 5))

img = img.convert("RGB")

img.save("output.jpg")

width, height = img.size

for h in range(height):
    for w in range(width):
        pixel_value = img.getpixel((w,h))
        print(pixel_value, end= ")")
    print()

# tugas 2 histogram gray
img = cv2.imread(file_name,0)

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255])
plt.title('histogram')

plt.show()