import numpy as np
import cv2

img=cv2.imread("face.jpg",1)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h=hsv[:,:,0]
s=hsv[:,:,1]
v=hsv[:,:,2]

hsv_split=np.concatenate((h,s,v),axis=1)

cv2.imshow("orignal",img)
cv2.imshow("split",hsv_split)

ret,min_sat=cv2.threshold(s,40,255,cv2.THRESH_BINARY)

ret,max_hue=cv2.threshold(h,20,255,cv2.THRESH_BINARY_INV)

final=cv2.bitwise_and(min_sat,max_hue)

cv2.imshow("min_sat",min_sat)
cv2.imshow("max_hue",max_hue)
cv2.imshow("final",final)

cv2.waitKey(0)
cv2.destroyAllWindows()
