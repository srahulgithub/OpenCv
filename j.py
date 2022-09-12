
import cv2
import numpy as np

# Let's load a simple image with 3 black squares
frame = cv2.imread('palm2.jpg')
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Find Canny edges
thresh = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('Canny Edges After Contouring', thresh)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contouring', frame)


cv2.imshow('img',frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
