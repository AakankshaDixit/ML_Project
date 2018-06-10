#!/usr/bin/python3

import cgi
import cgitb
import cv2

cgitb.enable()

print("Content-type:text/html")
print("")

data=cgi.FieldStorage()

# for reading the image
img =cv2.imread('panda.jpg')

image=img[0:450,0:800]
newimg=img[0:225,0:400]



if data.getvalue('a'):
	crop1=img[0:225,0:800]
	crop2=img[0:450,0:400]
	cv2.imshow('half image',crop1)
	cv2.imshow('half image2',crop2)
	

if choice=='2':
	print("1.top-left \n 2.top-right \n 3. bottom-left \n 4.bottom-right")
	ch=input("which one-fourth portion")
	

	if ch=='1':
		cropped=img[0:225,0:400]
		
	if ch=='2':
		cropped=img[0:225,400:800]

	if ch=='3':
		cropped=img[225:450,0:400]

	if ch=='4':
		cropped=img[225:450,400:800]
	
	cv2.imshow('one fourth',cropped)


if choice == '3':
	h=int(450/8)
	print(h)
	cropped_image=img[0:56, 0:100]
	cv2.imshow('one-eigth',cropped_image)
	
else:
	print("Wrong choice!!")

#for displaying the image
cv2.imshow('panda img',image)

cv2.waitKey(0)
cv2.destroyAllWindows()       




















