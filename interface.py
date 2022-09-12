import numpy as np
import cv2
cap = cv2.VideoCapture("hello.mp4")

color=(150,25,255)
width=-3
radius=5
point=(0,0)

def click(event,x,y,flags,pram):
    global point,pressed
    if event==cv2.EVENT_MOUSEMOVE:
        print("pressed",x,y)
        point=(x,y)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)

while(True):
    ret, frame = cap.read()

    #frame=cv2.resize(frame, f =1.5,fy =1.5)

    frame = cv2.resize(frame, (0,0), fx=1.5,fy=1.5)
    cv2.circle(frame,point,radius,color,width)
    cv2.imshow("Frame",frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
