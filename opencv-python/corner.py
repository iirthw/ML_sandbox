import cv2
import numpy as np

img = cv2.imread('assets/Nantes_lile_1.png')
img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
img_gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi Corner Detector (aka good features to track)
nb_corners = 100
quality = 0.01
min_dist_corners = 10
corners = cv2.goodFeaturesToTrack(img_gray_scale, nb_corners, quality, 
    min_dist_corners)

corners = np.int0(corners)

# draw corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
