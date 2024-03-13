import cv2
#ACtivity 2 all

image = cv2.imread('MAR10.jpg')

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
