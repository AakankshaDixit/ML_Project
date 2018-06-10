#!/usr/bin/python3

import cv2

#loading camera
#0 means first web cam , 1means second and so on ....

cam =cv2.VideoCapture(0)

#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc , 20.0,(640,480))

#checking for detection

while cam.isOpened():
	print("Working...")
	#real data of captured image stored in frame
	#processing and open status of camera stored in status
	status,frame=cam.read()
	
	out.write(frame)
	if status == True:
		frame= cv2.flip(frame,0)
	
		#write the flipped frame
		out.write(frame)
		
		newimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('camera0',frame) 
		#for i in range(10000):
		# 	cv2.imwrite()
		if cv2.waitKey(1) & 0xFF ==ord('q'):
			print("sdgaf")	
	
			
cam.release()
out.release()
cam.destroyAllWindows()
