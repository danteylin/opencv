import numpy as np
import cv2
img = cv2.imread("SKADI.png")
print(img.shape)
print(img.item(100,200,1))
#img[200:400,300:700]=0
roi=img[200:400,300:500] //201*401
img[100:300,300:500]=roi
print(img.size)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
