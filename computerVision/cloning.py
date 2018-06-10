import numpy as np
import cv2

img = cv2.imread('dog.jpeg',cv2.IMREAD_COLOR)

img[40,40] = [255,255,255]
px=img[40,40]
print(px)

# region of image
#roi = img[120:180, 120:180]
#print(roi) 

#img[30:100,170:220] = [255,255,255]

watch_face = img[40:115 , 110:200]
img[0:75 , 0:90]=watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
