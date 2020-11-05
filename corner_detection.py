import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

img = cv2.imread('board1.jpg')
img2 = cv2.imread('board1.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_bl = cv2.bilateralFilter(gray,100,100,1000)

corners = cv2.goodFeaturesToTrack(gray_bl, 90, 0.01, 100)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    img = cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',gray_bl)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()






