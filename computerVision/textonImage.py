#!/usr/bin/python3

import cv2

# reading image from the current location
img=cv2.imread("red1.jpeg",cv2.IMREAD_COLOR)

# writing text on image 
font = cv2.FONT_HERSHEY_SIMPLEX
textImage = cv2.putText(img,'the red smiley',(0,200),font , 1, (200,255,20), 2 ,cv2.LINE_AA)

cv2.imwrite('textedimg.png',textImage)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
