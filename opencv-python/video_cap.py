import numpy as np
import cv2

capture = cv2.VideoCapture(0)

isFirstFrame = True
while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))
    if isFirstFrame:
        isFirstFrame = False
        print("Video frame width: " + str(width))
        print("height frame height: " + str(height))

    image = np.zeros(frame.shape, np.uint8)
    shrunk_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # upper-left
    image[:height//2, :width//2] = cv2.rotate(shrunk_frame, cv2.cv2.ROTATE_180)
    # lower-left 
    image[height//2:, :width//2] = shrunk_frame
    # upper-right
    image[:height//2, width//2:] = cv2.rotate(shrunk_frame, cv2.cv2.ROTATE_180)
    # lower-right
    image[height//2:, width//2:] = shrunk_frame

    # draw a diagonal lime
    thicknessMedium = 5
    blueColor = (255, 0, 0) # bgr
    cv2.line(image, (0, 0), (width, height), blueColor, thicknessMedium)

    # draw a rectangle
    thicknessLight = 2
    greenColor = (0, 255, 0)
    p0 = (0, 0)
    p1 = (width // 2, height // 2)
    cv2.rectangle(image, p0, p1, greenColor, thicknessLight)

    # display text
    fontColor = (0, 10, 255)
    origin = (width//4, height//2 - 50)
    cv2.putText(image, "Test", 
        org=origin, fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
        fontScale=1, color=fontColor)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

capture.realse()
cv2.destroyAllWindows()