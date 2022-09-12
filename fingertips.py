import cv2
import numpy as np

img = cv2.imread("palm2.jpg",1)
cv2.imshow('palm image',img)

hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
skinRegionHSV = cv2.inRange(hsvim, lower, upper)
blurred = cv2.blur(skinRegionHSV, (2,2))
ret,thresh = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = max(contours, key=lambda x: cv2.contourArea(x))
cv2.drawContours(img, [contours], -1, (255,255,0), 2)
cv2.imshow("contours", img)

hull = cv2.convexHull(contours)
cv2.drawContours(img, [hull], -1, (0, 255, 255), 2)
cv2.imshow("hull", img)

hull = cv2.convexHull(contours, returnPoints=False)

M=cv2.moments(thresh)

cx=int(M["m10"]/M["m00"])
cy=int(M["m01"]/M["m00"])

cv2.circle(img,(cx,cy),5,(255,255,255),-1)

defects = cv2.convexityDefects(contours, hull)

if defects is not None:
  cnt = 0
for i in range(defects.shape[0]):
  s = defects[i][0]
  start[i][3] = tuple(contours[s][0])
  if cnt > 0:
   cnt = cnt+1

for i in range(defects.shape[0]):
    if start[i-1]-(1,1)<start[i]<start[i+1]+(1,1):
        continue
    else :
        cv2.circle(img, start[i], 4, [0, 0, 255], -1)

cv2.imshow("centroid", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
