import numpy as np
import cv2

bw=cv2.imread("kuro.jpg",0)
ht,wt=bw.shape[0:2]

cv2.imshow("bw",bw)

binary=np.zeros([ht,wt,1],'uint8')

thresh=160

for row in range (0,ht):
    for col in range (0,wt):
        if bw[row][col] > thresh:
            binary[row][col]=255

ret,threshb=cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)

thresha=cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,1)

cv2.imshow("threshslow",binary)
cv2.imshow("threshfast",threshb)
cv2.imshow("threshadapative",thresha)

cv2.waitKey(0)
cv2.destroyAllWindows()
