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
    print("9. ")
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
    
def option8():
    print("Activity 5 all")

def option9():
    print("You chose Option 9")
    
def plot_histogram(image, title):
    histogram = cv2.calcHist([image], [0], None, [256], [0,256])
    plt.plot(histogram, color='black')
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.show()
    

    

choice = 0
while choice != 10:
    main_menu()
    choice = int(input("Enter your choice (1-4): "))

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
        print("Invalid choice. Please enter a number between 1 and 4.")
