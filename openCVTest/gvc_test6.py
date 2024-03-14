import cv2
import numpy as np
import matplotlib.pyplot as plt
#Avtivity 4 all

image = cv2.imread('MAR10.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


histogram = cv2.calcHist([gray_image], [0], None, [256], [0,256])


edges = cv2.Canny(gray_image, 100, 200)


plt.figure(figsize=(12, 8))


plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')


plt.subplot(222)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(223)
plt.plot(histogram, color='black')
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')


plt.subplot(224)
plt.imshow(edges, cmap='gray')
plt.title('Edges of the Image')
plt.axis('off')

plt.tight_layout()
plt.show()
