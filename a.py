from __future__ import print_function
import cv2 
import argparse
import pytesseract
import numpy as np
from PIL import Image
from pytesseract import image_to_string

cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()
    #cv2.medianBlur(frame, 5)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,64])
    upper_red = np.array([180,38,255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    res= cv2.bitwise_and(frame, frame, mask = mask1)
    res = cv2.GaussianBlur(res,(3,3), 0)
    res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)    
    cv2.imshow('res', res)
    text = Image.fromarray(res)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(text, config='--psm 6 -c tessedit_char_whitelist=12345678ABCDEFGHIJKLMNOPQRSTUVWXYZ load_system_dawg=false load_freq_dawg=false')
    print(text)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release
    