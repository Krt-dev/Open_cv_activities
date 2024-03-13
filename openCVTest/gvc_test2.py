import cv2
#Activity 1 to get the pixel value

img = cv2.imread("MAR10.jpg", cv2.IMREAD_COLOR)

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