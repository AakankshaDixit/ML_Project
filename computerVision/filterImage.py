#!/usr/bin/python3

import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
	status,frame=cap.read()
	hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

	lower_read = np.array([56,4,80])
	upper_read = np.array([245,205,155])

	mask = cv2.inRange(hsv , lower_read , upper_read)
	res = cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow("frame1",frame)
	cv2.imshow("frame2",mask)
	cv2.imshow("frame3",res)

	if cv2.waitKey(1) and 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
