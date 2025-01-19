import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    _, frame = video.read()

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian',laplacian)

    edges = cv.Canny(frame, 100, 100)
    cv.imshow('Edges',edges)

    if cv.waitKey(5) == ord('x'):
        break

cv.destroyAllWindows()
video.release()
