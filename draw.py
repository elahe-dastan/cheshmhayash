import cv2 as cv
import numpy as np

# uint8 is basically the data-type of an image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
