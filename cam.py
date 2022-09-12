import cv2
import numpy as np



bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=30, detectShadows=False)

def bgSubMasking(self, frame):
    """Create a foreground (hand) mask
    @param frame: The video frame
    @return: A masked frame
    """
    fgmask = bgSubtractor.apply(frame, learningRate=0)

    kernel = np.ones((4, 4), np.uint8)

    # The effect is to remove the noise in the background
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)    # To close the holes in the objects
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Apply the mask on the frame and return
    return cv2.bitwise_and(frame, frame, mask=fgmask)


def threshold(mask):
    """Thresholding into a binary mask"""
    grayMask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayMask, 0, 255, 0)
    return thresh

def getMaxContours(contours):
    """Find the largest contour"""
    maxIndex = 0
    maxArea = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area > maxArea:
            maxArea = area
            maxIndex = i
    return contours[maxIndex]

thresh = threshold(mask)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)# There might be no contour when hand is not inside the frame
if len(contours) > 0:
    maxContour = getMaxContours(contours)


def countFingers(contour):
    hull = cv2.convexHull(contour, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(contour, hull)
        cnt = 0
        if type(defects) != type(None):
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(contour[s, 0])
                end = tuple(contour[e, 0])
                far = tuple(contour[f, 0])
                angle = calculateAngle(far, start, end)

                # Ignore the defects which are small and wide
                # Probably not fingers
                if d > 10000 and angle <= math.pi/2:
                    cnt += 1
        return True, cnt
    return False, 0

def calculateAngle(far, start, end):
    """Cosine rule"""
    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    angle = math.acos((b**2 + c**2 - a**2) / (2*b*c))
    return angle


def main():
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        pressed_key = cv2.waitKey(1)
        _,frame = capture.read()
        frame = cv2.flip(frame, 1)

        if pressed_key & 0xFF == ord('s'):
            hand_hist = bgSubMasking(frame)
            contours = threshold(hand_hist)



        cv2.imshow("Live Feed", rescale_frame(frame))

        if pressed_key & 0xFF == ord('e'):
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
