#!/usr/bin/python3

import cv2

def create_image(x,y,z):
	#most accurate result by cv2
	f_diff1 = cv2.absdiff(x,y)
	f_diff2 = cv2.absdiff(y,z)
	final_diff=cv2.bitwise_xor(f_diff1,f_diff2)
	return final_diff

cap=cv2.VideoCapture(0)
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]


diff_np=tp1-tp2
diff1 = cv2.subtract(tp1,tp2)
	
#converting image into gray
gray1=cv2.cvtColor(tp1, cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2, cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3, cv2.COLOR_BGR2GRAY)
	
while True:
	#performing bitwise operation
	final=create_image(gray1,gray2,gray3)
	cv2.imshow('diff_image',final)
	status,frame = cap.read()
	Frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray1=gray2
	gray2=gray3
	gray3=Frame

	if cv2.waitKey(1) and 0xff == ord('q'):
			break

cv2.release()	
cv2.destroyAllWindows()
