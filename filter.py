import numpy as np
import cv2

image=cv2.imread("kuro.jpg",1)
cv2.imshow("image",image)

blur=cv2.GaussianBlur(image,(55,5),100)

cv2.imshow("blur",blur)

kernel=np.ones((5,5),'uint8')

dilate =cv2.dilate(image,kernel,iterations=1)
erode=cv2.erode(image,kernel,iterations=1)

cv2.imshow("dilate",dilate)
cv2.imshow("erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
