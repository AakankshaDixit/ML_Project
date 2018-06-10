#!/usr/bin/python3
import cv2
import math
import numpy as np

img =cv2.imread('panda.jpg')

image=img[0:450,0:800]
newimg=img[0:225,0:400]
newimg1 = img[225:450 ,400:800]

#crop=cv2.circle(img,(100,160),25,(0,0,255),0)

#creating blank image
model=np.zeros((400,600,3))
cv2.imwrite('blank_page.jpg',model)

temp_img=cv2.imread('blank_page.jpg',1)

#print("blank",model)

#taking input for the center of the circle
h=int(input("enter value :"))
k=int(input("enter value :"))
r=int(input("enter value :"))

#loop for the cropping circlular img
for i in range(h-r,h+r):
	#circle's formula
	y=int(math.sqrt((r)**2-(i-h)**2))
	for j in range(k-y,k+y):
		temp_img[i][j][0]=img[i][j][0]
		temp_img[i][j][1]=img[i][j][1]
		temp_img[i][j][2]=img[i][j][2]

		img[i][j][0]=0
		img[i][j][1]=0
		img[i][j][2]=0

cv2.imshow('panda img',image)
#cv2.imshow('panda cropped',newimg)
cv2.imshow('panda cropped1',temp_img)
#cv2.imshow('panda cropped2',newimg1)
cv2.waitKey(0)
cv2.destroyAllWindows()       
