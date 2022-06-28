import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('../Face Detection/haar_face.xml')

people = []
DIR = 'train'
for i in os.listdir(DIR):
    people.append(i)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trained.yml')

img = cv.imread('val/jerry_seinfeld/3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (x,y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.putText(img, 'Con: '+ str(int(confidence)), (x,y+h+30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Detected Face', img)

cv.waitKey(0)