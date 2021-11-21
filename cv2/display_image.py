import cv2
import random

imgReadFlag = 1
img = cv2.imread('assets/lenna.png', imgReadFlag)
img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# cv2.imwrite("updatedImage.png", img)

offset = 50
for i in range(offset, 200):
    for j in range(offset, img.shape[1] - offset):
        img[i][j] = [random.randint(1, 255), random.randint(1, 255), 
            random.randint(1, 255)]

# copy sub-image pixels
tag = img[50:200, 50:200]
img[250:400, 250:400] = tag

cv2.imshow('lennaImage', img)

print(type(img))
print(img.shape)
print(img[0])

cv2.waitKey(0)
cv2.destroyAllWindows()