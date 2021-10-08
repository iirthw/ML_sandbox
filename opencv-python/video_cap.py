import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    #image = np.zeros()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.realse()
cv2.destroyAllWindows()