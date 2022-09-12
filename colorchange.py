import numpy as np
import cv2

color=cv2.imread("kuro.jpg",1)
cv2.imshow("image",color)
print(color.shape)
ht,wt,ch=color.shape

b,g,r=cv2.split(color)

rgb_split=np.empty([ht,wt*3,3],'uint8')

rgb_split[:,0:wt]=cv2.merge([b,b,b])
rgb_split[:,wt:wt*2]=cv2.merge([g,g,g])
rgb_split[:,wt*2:wt*3]=cv2.merge([r,r,r])

cv2.imshow("color",rgb_split)
cv2.moveWindow('color',0,ht)

cv2.waitKey(0)
cv2.destroyAllWindows()
