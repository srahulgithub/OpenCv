import numpy as np
import cv2

img=cv2.imread("kuro.jpg",1)
cv2.imshow("image",img)

imgh=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
imgs=cv2.resize(img,(500,500))
imgsn=cv2.resize(img,(500,500),interpolation=cv2.INTER_NEAREST)
imgsa=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)

cv2.imshow("img",img)
cv2.imshow("half",imgh)
cv2.imshow("stretch",imgs)
cv2.imshow("near",imgsn)
cv2.imshow("area",imgsa)

M=cv2.getRotationMatrix2D((0,0),-30,1)
rotate=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

cv2.imshow("rotate",rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
