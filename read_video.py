import cv2 as cv

capture = cv.VideoCapture('videos/vam.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(17) & 0xFF==ord('d'):
        break

# (-215:Assertion failed) openCV could not find the image or video frame at a particular location.

# release the capture pointer
capture.release()
cv.destroyAllWindows()
