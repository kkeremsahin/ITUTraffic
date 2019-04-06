from __future__ import print_function
import cv2 
import argparse
import pytesseract
import numpy as np
from PIL import Image
import math

cap = cv2.VideoCapture(0)


def draw_circle(img, radius, x, y):
    """
    Render circle
    :param img    : Canvas 
    :param radius : Radius of the circle
    :param x      : (x, y) is the center of the circle graph on the canvas
    :param y      : (x, y) is the center of the circle graph on the canvas
    """
    ############################################################
    #                  Write your code here!                   #
    ############################################################

    cv2.circle(img, (x, y), radius, (20, 215, 20), 10)

    ############################################################
    #                           End                            #
    ############################################################ 

while True:
    _, frame = cap.read()

    #frame = cv2.imread('B3.png')
    
    
    
    #whiteMask = np.zeros(frame.shape, dtype=np.uint8 )
    #whiteMask = abs(255-whiteMask)
    
    #cv2.imshow("a", whiteMask)

    median = cv2.medianBlur(frame, 5)
    medianGray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(medianGray, 240, 80)
    rows = edges.shape[0]
  
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1 , rows/8, param1=150, param2 =40, minRadius=40, maxRadius=300)
    

    

    if circles is not None:
        circles = np.uint16(np.round(circles))
        #print('AAA')
        #print(circles)
        #print('XXX')
        largest = circles[0,0]
        #print(largest)
        #print('O')
        #print(largest[2])

        for i in circles[0, :]:
            if i[2] > largest[2]:
                largest = i
        #cv2.circle(whiteMask, (largest[0], largest[1]), largest[2]-5, (0,0,0), -1)

        #for i in circles[0,:]:
         #   cv2.circle(whiteMask, (i[0], i[1]), i[2], (0,0,0), -1)
    
    #whiteMask = cv2.cvtColor(whiteMask,cv2.COLOR_BGR2GRAY)

    #masked = cv2.scaleAdd(whiteMask, 1, medianGray)
    
    last = cv2.getRectSubPix(medianGray, (3*largest[2],3*largest[2]),(largest[0], largest[1]))
    _, thr = cv2.threshold(last, 160, 255, cv2.THRESH_BINARY)

    Xcoord,Ycoord,Radius = largest[0],largest[1],largest[2] + 10;
    H, W = thr.shape
    # x and y coordinates per every pixel of the image
    x, y = np.meshgrid(np.arange(W), np.arange(H))
    # squared distance from the center of the circle
    d2 = (x - Xcoord)**2 + (y - Ycoord)**2
    # mask is True inside of the circle
    mask = d2 < Radius**2

    draw_circle(frame,largest[2],largest[0],largest[1])
    cv2.imshow('frame', frame)

    outside = np.ma.masked_where(mask, thr)
    average_color = outside.mean()
    thr[mask] = 0
    
    text = Image.fromarray(thr)
    cv2.imshow('thr', thr)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(text, config='--psm 6 -c tessedit_char_whitelist=123AB tessedit_char_blacklist=tIli)(8 load_system_dawg=false load_freq_dawg=false')
    print(text)

    #cv2.imshow("result", masked)
    #cv2.imshow("mask", whiteMask)
    cv2.imshow('last', last)
    

    '''if text == 'A1'or text == 'A|' or text == 'AI' or text == 'Al' or text =='Af':
        text = 'A1'

    if text == 'A2'or text == 'AZ' :
        text = 'A2'

    if text == 'A3'or text == 'A8' or text == 'AB': 
        text = 'A3'

    if text == 'B1'or text == 'B|' or text == 'BI' or text == 'Bl' or text =='Bf' or text == '31':
        text = 'A1'
'''

    k = cv2.waitKey(5) & 0xFF

    if k==27:
        break

cv2.destroyAllWindows()
cap.release


'''
2-> 2, z, 
'''