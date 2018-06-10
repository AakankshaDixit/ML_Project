
import cv2  
import matplotlib             

#version must be 3.4.1
cv2.__version__

#reading imag in color mode      (by default is 1)
          #cv2.imread=1  ---- we can write like this also
#img.shape

img1=cv2.imread('/home/aakanksha/Desktop/ML/index.jpeg',0)           #all part become black and white
#img1.shape  
image=img1[0:400,0:500]

newimg =img1[0:100,0:160]
print(newimg.shape)
(h,w) = image.shape[:2]
center = (w/2, h/2)

#rotate the image by particular amount of degree
M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(image, M , (w,h))


#Mat croppedFrame = frame(Rect(0, frame.rows/2, frame.cols, frame.rows/2));



#cv2.line(img,(0,0),(300,524),(255,0,0),2)
cv2.imshow('flower original',image)
cv2.imshow("rotated",rotated)





#cv2.imshow('flower cropped',croppedFrame)

cv2.waitKey(0)

cv2.destroyALLWindows()

