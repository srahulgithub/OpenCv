import numpy as np
import cv2

img=cv2.imread("tomato.png",1)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
res,thresh=cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)

cv2.imshow("thresh",thresh)

edges=cv2.Canny(img,100,70)
cv2.imshow("canny",edges)

final=cv2.bitwise_and(thresh,edges)
cv2.imshow("final",final)

cv2.waitKey(0)
cv2.destroyAllWindows()
