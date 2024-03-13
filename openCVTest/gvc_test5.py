import cv2
import numpy as np
import matplotlib.pyplot as plt
#Activity 3 all
def plot_histogram(image, title):
    histogram = cv2.calcHist([image], [0], None, [256], [0,256])
    plt.plot(histogram, color='black')
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.show()


original_image = cv2.imread('MAR10.jpg')


original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)


plt.imshow(original_image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()


plot_histogram(original_image, 'Histogram of Original Image')


blue_channel = original_image[:, :, 0]
green_channel = original_image[:, :, 1]
red_channel = original_image[:, :, 2]


plot_histogram(blue_channel, 'Blue Channel Histogram')
plot_histogram(green_channel, 'Green Channel Histogram')
plot_histogram(red_channel, 'Red Channel Histogram')
