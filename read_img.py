import cv2 as cv

# img is a numpy ndarray with shape (width, height, channel=3)
img = cv.imread('images/pandas_at_table.jpg')

cv.imshow('pandas at table', img)

# wait an infinite time for a key to be pressed
cv.waitKey(0)
