import cv2

imgReadFlag = 1
img = cv2.imread('assets/lenna.png', imgReadFlag)
img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# cv2.imwrite("updatedImage.png", img)

cv2.imshow('lennaImage', img)

print(type(img))

cv2.waitKey(0)
cv2.destroyAllWindows()