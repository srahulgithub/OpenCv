import numpy as np
import cv2

canvas=np.ones([500,500,3],'uint8')*255

color=(26,6,77)
radius=3
pressed=False
pressed2=False

colorr=(255,255,255)

def click(event,x,y,flags,pram):
    global canvas,pressed,pressed2
    if event==cv2.EVENT_LBUTTONDOWN:
        pressed=True
        cv2.circle(canvas,(x,y),radius,color,-1)
    elif event==cv2.EVENT_LBUTTONUP:
        pressed=False
    elif event==cv2.EVENT_MOUSEMOVE:
        if pressed==True:
            cv2.circle(canvas,(x,y),radius,color,-1)
        elif pressed2==True:
            cv2.rectangle(canvas,(x,y),(x+4,y+4),colorr,-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        pressed2=True
        cv2.circle(canvas,(x,y),6,colorr,-1)
    elif event==cv2.EVENT_RBUTTONUP:
        pressed2=False





cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)

while(True):

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color=(255,0,0)
    elif ch & 0xFF==ord('g'):
            color=(0,255,0)
    elif ch & 0xFF==ord('r'):
        color=(0,0,255)

    cv2.imshow("canvas",canvas)



cv2.destroyAllWindows()
