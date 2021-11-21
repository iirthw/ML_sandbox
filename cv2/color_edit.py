import cv2
import random

def main():
    imgReadFlag = 1
    img = cv2.imread('assets/lenna.png', imgReadFlag)
    img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)

    cv2.imshow('lennaImage', img)

    print(type(img))
    print(img.shape)
    print(img[0])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()