import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('videos/vam.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(17) & 0xFF == ord('d'):
        break

# (-215:Assertion failed) openCV could not find the image or video frame at a particular location.

# release the capture pointer
capture.release()
cv.destroyAllWindows()
