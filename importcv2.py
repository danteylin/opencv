import numpy as np
import cv2
img = cv2.imread("SKADI.png")
print(img.shape)
print(img.item(100,200,1))
roi = img[200:400,300:500]  //201*401
roi[:,:,1]=255
# roi[:,:,2]=0
h,w,a =roi.shape
img[100:300,300:500] = roi
img[200:400,200:400] = roi
print(len(roi),len(roi[0]))
img[10:10+h,10:10+w] = roi
print(img.size)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
