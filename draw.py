import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
img = cv.imread('Resources/photos/cat.jpg')

# Paint the image a certain colour
#blank[:] = 0,0,255 # BGR
#cv.imshow('Red', blank)

# Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (255,255,255), thickness=-1)
cv.imshow('Circle', blank)


# Draw a line
cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (blank.shape[1], blank.shape[0]), (255,255,0), thickness=2)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, "Hello, I'm ADP", (0, 350), cv.FONT_HERSHEY_COMPLEX, 2.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)