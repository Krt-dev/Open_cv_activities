import cv2
import numpy as np
import matplotlib.pyplot as plt
#Activity 5 all
def display_image_with_edges_and_histogram(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray_image, 100, 200)
    
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    
    plt.figure(figsize=(12, 8))


    plt.subplot(221)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')


    plt.subplot(222)
    plt.imshow(edges, cmap='gray')
    plt.title('Edges of the Image')
    plt.axis('off')

    plt.subplot(223)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')


    plt.subplot(224)
    plt.plot(histogram, color='black')
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

def print_image_properties(image):
    
    filename = "MAR10.jpg"  
    format = "RGB"  
    height, width, _ = image.shape
    size = image.size
    
    print("Image Properties:")
    print("Filename:", filename)
    print("Format:", format)
    print("Width:", width)
    print("Height:", height)
    print("Size:", size)

def get_pixel_value(image, x, y):
    b, g, r = image[y, x]
    print("Pixel value at ({}, {}): (R={}, G={}, B={})".format(x, y, r, g, b))


image = cv2.imread('MAR10.jpg')

display_image_with_edges_and_histogram(image)


print_image_properties(image)


x = 100 
y = 50   
get_pixel_value(image, x, y)
