import numpy as np
import cv2 as cv
# 用灰度模式加载图像
img = cv.imread('SKADI.png')

print(len(img),len(img[0]))
cv.line(img,(200,100),(500,500),(255,0,0),5)
cv.rectangle(img,(100,0),(300,300),(0,255,0),3)
cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('messigray.png',img) 