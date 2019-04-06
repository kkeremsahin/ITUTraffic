import numpy as np
import cv2
import argparse
threshold_arrow=0.1

img1=cv2.imread("tabela.jpg",cv2.IMREAD_GRAYSCALE)
img=cv2.imread("circle.jpg",cv2.IMREAD_GRAYSCALE)
threshold1=cv2.inRange(img1,0,175)
threshold2=cv2.inRange(img,0,175)


distance = cv2.matchShapes(threshold2,threshold1,cv2.CONTOURS_MATCH_I2,0)
if(distance<threshold_arrow):
    print("It's an arrow")
else:
    print("Not an arrow")



cv2.waitKey(0)
cv2.destroyAllWindows()
