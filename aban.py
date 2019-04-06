from __future__ import print_function
import cv2 as cv
import argparse
import pytesseract as ts
import numpy as np
from PIL import Image
from pytesseract import image_to_string
import time
import math



#if image is to be read
#image='B3.png'

#if not uncomment this
cap = cv.VideoCapture(0)


# N dimensional array reference for you ;))
mahmut = np.ndarray(shape=(3,3), dtype=float, order='F')
print (mahmut)


while True:

    # image input
    #frame = cv.imread(image, cv.IMREAD_GRAYSCALE)

    # camera input
    _, frame = cap.read()
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)


    # eliminate noise 
    frame = cv.GaussianBlur(frame,(3,3), 2)

    # find circles
    circles = cv.HoughCircles(frame, cv.HOUGH_GRADIENT, 1 , frame.shape[0]//8  , param1 = 150 ,param2=80, minRadius=20, maxRadius=300)


    if circles is not None:

        largestCircle = circles[0][0]

        for i in circles[0,:]:
            cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            
            if i[2] > largestCircle[2]:
                largestCircle = i
        
        #debug
        #print(largestCircle)
        

        insideOfCircle = cv.getRectSubPix(frame, (math.ceil(1.5*largestCircle[2]),math.ceil(1.5*largestCircle[2])),(largestCircle[0], largestCircle[1]))
        _, result = cv.threshold(insideOfCircle, 100, 255, cv.THRESH_BINARY)

        
        result = cv.GaussianBlur(result,(3,3), 2)
        cv.imshow('Result',result)

        ts.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = ts.image_to_string(result, config="-c tessedit_char_whitelist=123AB tessedit_char_blacklist=il74567890zZ| --psm 6")
        print(text)


    #show the last frame wait for 10 ms
    cv.imshow('Big Picture',frame)

    k = cv.waitKey(5) & 0xFF

    #esc to exit
    if k==27:
        break

cv.destroyAllWindows()
#cap.release