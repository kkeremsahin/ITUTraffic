import cv2 as cv
import numpy as np
import matplotlib
import math
import argparse
import time
threshold_arrow=0.005
arrow=cv.imread('tabela.jpg',cv.IMREAD_GRAYSCALE)
arrow = cv.inRange(arrow, 0, 100,dst=None)
cv.imshow('arrow',arrow)


def is_arrow(thresholded_image):
    distance = cv.matchShapes(thresholded_image,arrow,cv.CONTOURS_MATCH_I2,0)
    if(distance<threshold_arrow):
        return True
    else:
        return False

cap = cv.VideoCapture(0)
mahmut = np.ndarray(shape=(3,3), dtype=float, order='F')

while True:
    _, frame = cap.read()
    #time.sleep(0.5)
    #color convertion bgr to gray
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #gaussian blur
    frame = cv.GaussianBlur(frame, (3, 3), 2)

    # find circles
    circles = cv.HoughCircles(frame, cv.HOUGH_GRADIENT, 1, frame.shape[0] // 8, param1=150, param2=80, minRadius=20,maxRadius=300)

    if circles is not None:

        largestCircle = circles[0][0]

        for i in circles[0, :]:
            cv.circle(frame, (i[0], i[1]), i[2], (255), 5)

            if i[2] > largestCircle[2]:
                largestCircle = i

        # debug
        # print(largestCircle)

        insideOfCircle = cv.getRectSubPix(frame, (math.ceil(1.8 * largestCircle[2]), math.ceil(1.5 * largestCircle[2])),(largestCircle[0], largestCircle[1]))
        result = cv.inRange(insideOfCircle, 0, 100,dst=None)

        result = cv.medianBlur(result,5,dst=None)
        print(is_arrow(result))
        if is_arrow(result):
            contours = cv.findContours(result.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            # finds corners

            # cv.imshow('grayscale',image)
            # cv.imshow('binary',binarized)
            corners = cv.goodFeaturesToTrack(result, 20, 0.01, 20)
            corners = np.int0(corners)

            # plt.imshow(img),plt.show()
            for c in contours[0]:
                M = cv.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                cv.drawContours(result, [c], -1, (0, 255, 0), 2)
                cv.circle(result, (cX, cY), 7, (0, 0, 0), -1)
                cv.putText(result, "center", (cX - 20, cY - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            for i in corners:
                x, y = i.ravel()
                if abs(cX - x) < 10 or abs(cY - y) < 10:
                    cv.circle(result, (x, y), 4, [0, 0, 0], -1)
                    cv.putText(result, "pointy", (x - 20, y - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    pointy_X = x
                    pointy_Y = y

            #print(cX, pointy_X, cY, pointy_Y)


            if abs(cX - pointy_X) < 10 and cY - pointy_Y < 0:
                cv.putText(result, "Down Arrow", (cX + 20, cY + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            elif abs(cX - pointy_X) < 10 and cY - pointy_Y > 0:
                cv.putText(result, "UP Arrow", (cX + 20, cY + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            elif abs(cY - pointy_Y) < 10 and cX - pointy_X > 0:
                cv.putText(result, "left Arrow", (cX + 20, cY + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            elif abs(cY - pointy_Y) < 10 and cX - pointy_X < 0:
                cv.putText(result, "Right Arrow", (cX + 20, cY + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            else:
                print('none')




        cv.imshow('Result', result)

    cv.imshow('Big Picture', frame)

    k = cv.waitKey(5) & 0xFF

    # esc to exit
    if k == 27:
        break

cv.destroyAllWindows()






