import cv2 as cv
import numpy as np

img = cv.imread('images/pandas_at_table.jpg')
cv.imshow('pandas at table', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(gray, 125, 175)
cv.imshow('canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('canny_blur', canny_blur)

contours_blur, hierarchies_blur = cv.findContours(canny_blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours_blur)} contours found')

# threshold essentially looks at an image and tries to binarize that image so if a particular pixel's density is below
# 125 it's going to be set to zero or black and if it's above 125 it's going to be set to white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours_thresh, hierarchies_thresh = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours_thresh)} contours found')

cv.drawContours(blank, contours_thresh, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
