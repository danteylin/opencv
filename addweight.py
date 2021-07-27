import numpy as np
import cv2
img = cv2.imread("SKADI.png")
roi1 = img[200:400,300:500]
roi2= img[100:300,300:500]
dst=cv2.addWeighted(roi1,0.7,roi2,0.3,0)
img[200:400,300:500]=dst
# roi[:,:,2]=0
print(img.size)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()