#!/usr/bin/python3

import kairos_face

kairos_face.settings.app_id = 'id'
kairos_face.settings.app_key =  'key'


# enrolling new student into the database
def enroll(image_file):
	# Enrolling from a file
	data=kairos_face.enroll_face(file=image_file, subject_id='subject1', gallery_name='student')
	print(data)


#to detect a face from the image
def detect(image_name):
	# Detect from a file
	recognized_faces = kairos_face.detect_face(file=image_name, gallery_name='student')
	print(recognized_faces)

#identify a face from an existing file
def recognize(local_image):
	# Recognizing from a file
	recognized_faces = kairos_face.recognize_face(file=local_image, gallery_name='student')
	print(recognized_faces)


#options
choice='''
	1.detect
	2.enroll
	3.recognize
'''

print(choice)

ch= input("enter your choice")

if ch == '1':
	name=input("enter the image name")
	detect(name)

elif ch == '2':
	name=input("enter the image name")
	enroll(name)

elif ch == '3':
	name=input("enter the image name")
	recognize(name)

else:
	print("sorry!!")
