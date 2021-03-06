import cv2 as cv

img = cv.imread('images/pandas_at_table.jpg')
cv.imshow('pandas at table', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Blur
# kernel size is the window size that open cv uses to compute the blown image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('canny_blur', canny_blur)

# Dilating the image
dilated = cv.dilate(img, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# Cropping
cropped = img[500:600, 600:700]
cv.imshow('cropped', cropped)

cv.waitKey(0)
