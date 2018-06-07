import cv2

img =cv2.imread('panda.jpg')

image=img[0:450,0:800]
newimg=img[0:225,0:400]
#newimg1 = img[225:450 ,400:800]
h=450/2
w=800


print("enter your choice:")
print("1.cut in half")
print("2.cut in one-fourth")
print("3.cut in one-eigth")
 
choice =input()

if choice == '1':
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


cv2.imshow('panda img',image)

cv2.waitKey(0)
cv2.destroyAllWindows()       




















