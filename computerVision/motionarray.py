#!/usr/bin/python3

import cv2
import numpy as np
import time


cam =cv2.VideoCapture(0)
listarr=[]
while cam.isOpened():
	print("Working...")
	#real data of captured image stored in frame
	#processing and open status of camera stored in status
	for i in range(0,5):
		status,frame=cam.read()

		c= cv2.imwrite("frame"+str(i)+".png" ,frame)
		
		cp=np.asarray(c,dtype=np.int32)
		np.savetxt("frame"+str(i)+".csv",cp,delimiter=',')
		
		data=np.load("frame"+str(i)+".npy")	
		listarr.append(data)
			
		time.sleep(2)
	
	print(listarr)
	
	newimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	print(frame)
	
	#cv2.imwrite("frame1",frame)
	cv2.imshow('camera0',newimg) 
	#for i in range(10000):
	# 	cv2.imwrite()
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break	
	
			
cam.release()
cam.destroyAllWindows()
