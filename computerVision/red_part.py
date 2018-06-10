#!/usr/bin/python3
import cv2

#starting camera
cap = cv2.VideoCapture(0)

#loading image
#img = cv2.imread('red1.jpeg')
#print(img.shape)

#only_red = cv2.inRange(img,(0,0,40),(20,20,255))
#checking web cam
while cap.isOpened():
         #true , false ,image frame
	status,frame=cap.read()
                                  #starting color , end color
	
	only_green = cv2.inRange(frame,(40,0,0),(255,20,20))
	#cv2.imshow('windows_red',only_red)
	cv2.imshow('window_green',only_green)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
