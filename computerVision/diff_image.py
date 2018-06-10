#!/usr/bin/python3

import cv2

cap=cv2.VideoCapture(0)

tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]

diff_np=tp1-tp2
diff1 = cv2.subtract(tp1,tp2)

#most accurate result by cv2
f_diff1 = cv2.absdiff(tp1,tp2)
f_diff2 = cv2.absdiff(tp2,tp3)
#performing bitwise operation
final_diff=cv2.bitwise_and(f_diff1,f_diff2)

cv2.imshow("Bitwise Image",final_diff)
cv2.waitKey(1)
cv2.destroyAllWindows()
