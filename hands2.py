
import cv2
import numpy as np


# Let's load a simple image with 3 black squares
img = cv2.imread('palm2.jpg')
cv2.waitKey(0)
frame=img.copy()

# Grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Find Canny edges
thresh = cv2.Canny(gray, 250, 200)

cv2.imshow('Canny ', thresh)

cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv2.drawContours(img, contours, -1, (255,255,0), 2)
cv2.imshow("cent", img)

cv2.waitKey(0)

filtered=[]
for c in contours:
    if cv2.contourArea(c) < 200 : continue
    filtered.append(c)
print(len(filtered))
cv2.waitKey(0)

for c in filtered:
    cv2.drawContours(img, [c], -1, (255,255,0), 2)
#filter = max(filter, key=lambda x: cv2.contourArea(x))

cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
for c in filtered:
    hull = cv2.convexHull(c)
    cv2.drawContours(img, [hull], -1, (0, 255, 255), 2)
    cv2.imshow("hull", img)
    hull = cv2.convexHull(filter, returnPoints=False)
    M=cv2.moments(thresh)
    cx=int(M["m10"]/M["m00"])
    cy=int(M["m01"]/M["m00"])
    cv2.circle(img,(cx,cy),5,(255,255,255),-1)
    defects = cv2.convexityDefects(c, hull)
    if defects is not None:
      cnt = 0
    for i in range(defects.shape[0]):
      s, e, f, d = defects[i][0]
      start = tuple(c[s][0])
      end = tuple(c[e][0])
      far = tuple(c[f][0])
      cv2.circle(img, start, 4, [0, 0, 255], -1)
      cv2.circle(img, end, 4, [0, 0, 255], -1)
      if cnt > 0:
       cnt = cnt+1
    cv2.imshow("centroid", img)





cv2.waitKey(0)
cv2.destroyAllWindows()
