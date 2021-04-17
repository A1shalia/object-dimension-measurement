import numpy as np
import cv2
import utils

#webcam value when set to false, will use source image at path
webcam = False

#Pass the path of source image
path = '2.jpg'

imgCapture = cv2.VideoCapture(0)
imgCapture.set(10, 160)
imgCapture.set(3, 1920)
imgCapture.set(4, 1080)
#define scale
scale = 2
wP = 210*scale
hP = 297*scale

while True:
    if webcam:
        success, img = imgCapture.read()
    else:
        img = cv2.imread(path)

    imgContours, Contours1 = utils.getContours(img, minArea=50000, filter=4)
    if len(Contours1) != 0:
        biggest = Contours1[0][2]
        # print(biggest)
        imgWarp = utils.warpImg(img, biggest, wP, hP)
        #cv2.imshow('A4', imgWarp)
        imgContours2, Contours2 = utils.getContours(imgWarp, minArea=2000, filter=4,
                                                    cThresh=[50, 50], draw = False)
        if len(Contours1)!=0:
            for obj in Contours2:
                cv2.polylines(imgContours2, [obj[2]], True, (0,255,0), 2)
                newPoints = utils.reorder(obj[2])
                #Divide no of pixels by the scale value
                newWidth = round((utils.findDist(newPoints[0][0]//scale, newPoints[1][0]//scale)/10), 1)
                newHeight = round((utils.findDist(newPoints[0][0]//scale, newPoints[2][0]//scale)/10), 1)
                cv2.arrowedLine(imgContours2, (newPoints[0][0][0], newPoints[0][0][1]),
                                (newPoints[1][0][0], newPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (newPoints[0][0][0], newPoints[0][0][1]),
                                (newPoints[2][0][0], newPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, '{}cm'.format(newWidth), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
                cv2.putText(imgContours2, '{}cm'.format(newHeight), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)

        cv2.imshow('A4', imgContours2)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    #Print original image
    cv2.imshow("Original", img)
    cv2.waitKey(1)
