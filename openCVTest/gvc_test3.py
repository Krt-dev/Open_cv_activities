import cv2
#Activity 1 to convert to black and white
image = cv2.imread('MAR10.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)  
cv2.destroyAllWindows() 
