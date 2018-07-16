#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:35:23 2018

@author: apple
"""
import cv2
import numpy as np

#camera = cv2.VideoCapture ("video.avi")

#camera.open("video.avi")
car_cascade = cv2.CascadeClassifier('/Users/apple/Desktop/Project/GitHub/Car-detection/cars.xml')
while True:
    #(grabbed,frame) = camera.read()
    img = cv2.imread('/Users/apple/Desktop/web/Toyota2b.jpg')
    #grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars:
     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
     #cv2.imshow("video",frame)
     cv2.imwrite('/Users/apple/Desktop/web/cardetect.jpg',img)
    """if cv2.waitKey(1)== ord('q'):
        break
#camera.release()
#cv2.destroyAllWindows()"""