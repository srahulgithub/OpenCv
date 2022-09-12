import numpy as np
import cv2
import random

img=cv2.imread("fuzzy.png",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)

thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,205,1)

kernel=np.ones((5,5),'uint8')

dilate =cv2.dilate(thresh,kernel,iterations=1)

cv2.imshow("fuzzy",img)
cv2.imshow("binary",thresh)
cv2.imshow("dilate",dilate)

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

contours2,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours2))

filtered=[]
for c in contours:
    if cv2.contourArea(c) < 1000 : continue
    filtered.append(c)
print(len(filtered))

objects=np.zeros([img.shape[0],img.shape[1],3],'uint8')
for c in filtered:
    col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cv2.drawContours(objects,[c],-1,col,-1)
    area=cv2.contourArea(c)
    p=cv2.arcLength(c,True)
    print(area,p)
cv2.imshow("contours",objects)

filtered2=[]
for c2 in contours2:
    if cv2.contourArea(c2) < 1000 : continue
    filtered2.append(c2)
print(len(filtered2))

objects2=np.zeros([img.shape[0],img.shape[1],3],'uint8')
for c2 in filtered2:
    col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cv2.drawContours(objects2,[c2],-1,col,-1)
    area=cv2.contourArea(c)
    p=cv2.arcLength(c,True)
    print(area,p)
cv2.imshow("contours2",objects2)

cv2.waitKey(0)
cv2.destroyAllWindows()
