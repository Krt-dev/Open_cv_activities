import cv2
import numpy as np
#Activity 1 to convert image to different flags

inpImag = "MAR10.jpg"

#Displays image as is
img = cv2.imread(inpImag, cv2.IMREAD_COLOR)
#Grayscale
#img = cv2.imread("MAR10.jpg", cv2.IMREAD_GRAYSCALE)
#No changes
#img = cv2.imread("MAR10.jpg", cv2.IMREAD_UNCHANGED)


cv2.imshow("image", img)


cv2.waitKey(0)


cv2.destroyAllWindows()
