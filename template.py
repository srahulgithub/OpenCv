import numpy as np
import cv2

image=cv2.imread("palm.jpg",1)
frame=cv2.imread("palm.jpg",0)
temp=cv2.imread("tips.png",0)

cv2.imshow("kuro",frame)
cv2.imshow("ball",temp)

result=cv2.matchTemplate(frame,temp,cv2.TM_CCOEFF_NORMED)
minval,maxval,minloc,maxloc=cv2.minMaxLoc(result)
print(maxval,maxloc)
cv2.circle(result,maxloc,15,255,2)
cv2.circle(image,maxloc,15,255,2)
cv2.imshow("result",result)
cv2.imshow("final",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
