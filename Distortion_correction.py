import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator

img = cv2.imread('board1.jpg')
scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

points = []
def getpoint(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append([x,y])


cv2.namedWindow('image')
cv2.setMouseCallback('image',getpoint)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

pts1 = np.float32(points)
pts2 = np.float32([[0,0],[512,0],[0,512],[512,512]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(512,512))

dst = cv2.rotate(dst, cv2.ROTATE_90_CLOCKWISE)
dst = cv2.rotate(dst, cv2.ROTATE_90_CLOCKWISE)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',dst)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
