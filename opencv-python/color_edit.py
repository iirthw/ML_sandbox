import cv2
import random

def shape_selection(event, x, y, flags, param):
    # See https://stackoverflow.com/questions/60113239/how-to-make-rectangle-visible-while-selecting-a-area-in-image
    global coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates = [(x, y)]
        coordinates.append((x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if len(coordinates) == 2:
            coordinates.pop(1)
            coordinates.append((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        coordinates.pop(1)
        coordinates.append((x,y))
    if len(coordinates) == 2:
        image[:] = image_copy[:]
        cv2.rectangle(image, coordinates[0], coordinates[1], (0, 0, 255), 1)
        cv2.imshow("image", image)

imgReadFlag = 1
img = cv2.imread('assets/lenna.png', imgReadFlag)
img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

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