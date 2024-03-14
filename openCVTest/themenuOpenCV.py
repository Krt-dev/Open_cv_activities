import cv2
import numpy as np
import matplotlib.pyplot as plt

def main_menu():
    print("Open CV activities!")
    print("1. Display Image")
    print("2. Display and Grayscale")
    print("3. Get Pixel value")
    print("4. Convert to back and white")
    print("5. Activity 2 all")
    print("6. Activity 3 all")
    print("7. Activity 4 all")
    print("8. Activity 5 all")
    print("9. Secret message")
    print("10. Exit")

def option1():
    print("Display Image")
    img = cv2.imread("D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def option2():
    print("Display and Grayscale")
    img = cv2.imread("D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def option3():
    print("Get pixel value")
    img = cv2.imread("D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg", cv2.IMREAD_COLOR)
    #input pixel
    x = 100  
    y = 50   

    b, g, r = img[y, x]

    print("BGR values at pixel (x={}, y={}):".format(x, y))
    print("Blue: ", b)
    print("Green: ", g)
    print("Red: ", r)

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def option4():
    print("Convert to black and white")
    image = cv2.imread('D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows() 
    
    
def option5():
    print("Activity 2 all")
    image = cv2.imread('D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg')

    height, width, channels = image.shape
    print("Image size: {} x {}".format(width, height))


    x = 100  
    y = 50  
    b, g, r = image[y, x]
    print("Pixel value at ({}, {}): (R={}, G={}, B={})".format(x, y, r, g, b))


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges1 = cv2.Canny(gray_image, 100, 200)
    edges2 = cv2.Canny(gray_image, 50, 150)
    edges3 = cv2.Canny(gray_image, 150, 250)
    edges4 = cv2.Canny(gray_image, 200, 250)
    cv2.imshow('Edges 1 =', edges1)
    cv2.imshow('Edges 2 =', edges2)
    cv2.imshow('Edges 3 =', edges3)
    cv2.imshow('Edges 4=', edges4)


    blue_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    red_channel = image[:, :, 2]

    cv2.imshow('Blue Channel', blue_channel)
    cv2.imshow('Green Channel', green_channel)
    cv2.imshow('Red Channel', red_channel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def option6():
    print("Activity 3 all")
    original_image = cv2.imread('D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg')
    second_image = cv2.imread('D:\Repos\Open_cv_activities\openCVTest\Images\Log in required.png')

    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    second_image_rgb = cv2.cvtColor(second_image, cv2.COLOR_BGR2RGB)

   
    plt.subplot(2, 2, 1)
    plt.imshow(original_image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(second_image_rgb)
    plt.title('Second Image')
    plt.axis('off')

  
    plt.subplot(2, 2, 3)
    plot_histogram(original_image, 'Histogram of Original Image')

    plt.subplot(2, 2, 4)
    plot_histogram(second_image, 'Histogram of Second Image')

    plt.tight_layout()
    plt.show()
    
def option7():
    print("Activity 4 all")
    image = cv2.imread('D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg')


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
    
def option8():
    print("Activity 5 all")
    image = cv2.imread('D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg')

    display_image_with_edges_and_histogram(image)

    print_image_properties(image)
    x = 100 
    y = 50   
    get_pixel_value(image, x, y)

def option9():
    print("Flat 1 lang miss pls huhuhuhu")
    
def plot_histogram(image, title):
    histogram = cv2.calcHist([image], [0], None, [256], [0,256])
    plt.plot(histogram, color='black')
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.show()
    
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
    
    filename = "D:\Repos\Open_cv_activities\openCVTest\Images\MAR10.jpg"  
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
    
def plot_histogram(image, title):
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=col)
        plt.xlim([0, 256])
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    

choice = 0
while choice != 10:
    main_menu()
    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        option1()
    elif choice == 2:
        option2()
    elif choice == 3:
        option3()
    elif choice == 4:
        option4()
    elif choice == 5:
        option5()
    elif choice == 6:
        option6()
    elif choice == 7:
        option7()
    elif choice == 8:
        option7()
    elif choice == 9:
        option7()
    elif choice == 10:
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
