from random import gauss
import cv2 as cv

img = cv.imread('Resources/photos/cats.jpg')
#cv.imshow('Cat', img)

# Average
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussina Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median blur
median = cv.medianBlur(img, 3 )
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)