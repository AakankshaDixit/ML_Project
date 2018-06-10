#!/usr/bin/python3
import cv2

img1 = cv2.imread('dog.jpeg')
img2 = cv2.imread('images.jpeg')


print(img1.shape)
print(img2.shape)


newimg = cv2.addWeighted(img2,0.8,img1,0.6,0)

cv2.imshow('windows',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

