import numpy as np
import cv2

img=cv2.imread("blob.png",1)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
thresh =cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,95,1)
cv2.imshow("binary",thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE,)

img2=img.copy()

index=-1
thickness=2
color=(255,2,30)
cv2.drawContours(img2,contours,index,color,thickness)

cv2.imshow("count",img2)
cv2.imshow("gray",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
