
import cv2 as cv
# 用灰度模式加载图像
R=0
G=0
B=0
S=1
def nothing(x):
    global R,G,B,S
    R = cv.getTrackbarPos('R','image')
    G = cv.getTrackbarPos('G','image')
    B = cv.getTrackbarPos('B','image')
    S = cv.getTrackbarPos('S','image')

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),100,(B,G,R),S)


img = cv.imread('SKADI.png')

cv.namedWindow('image',cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('image',draw_circle)
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('S','image',1,10,nothing)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
