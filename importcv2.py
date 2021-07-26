
import cv2 as cv
# 用灰度模式加载图像
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),100,(255,0,0),3)


img = cv.imread('SKADI.png',0)

cv.namedWindow('image',cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
