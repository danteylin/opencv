import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('SKADI.png', 0)

laplacian = cv2.Laplacian(img, -1)

sobel = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=5)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobelx1 = cv2.Sobel(img, -1, 1, 0, ksize=-1)  # ksize=-1同样可以实现scharr
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)
sobelx64f1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
abs_sobel64f1 = np.absolute(sobelx64f1)
sobel_8u1 = np.uint8(abs_sobel64f1)

scharr = cv2.Scharr(img, cv2.CV_8U, 0, 1)
scharrx64f1 = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharrx = cv2.Scharr(img, cv2.CV_8U, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_8U, 0, 1)
scharry64f1 = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharrxy = cv2.addWeighted(scharrx64f1,0.5,scharry64f1,0.5,0)


plt.subplot(241), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(242), plt.imshow(sobel_8u1, cmap='gray'), plt.title('Sobel abs(CV_64F)')
#plt.subplot(242), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.subplot(243), plt.imshow(sobel, cmap='gray'), plt.title('Sobel')
plt.subplot(244), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
plt.subplot(245), plt.imshow(sobelx1, cmap='gray'), plt.title('Scharr X')
plt.subplot(246), plt.imshow(scharrx, cmap='gray'), plt.title('Scharr X')
plt.subplot(247), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y')
#plt.subplot(248), plt.imshow(scharry, cmap='gray'), plt.title('Scharr Y')
plt.subplot(248), plt.imshow(scharrxy, cmap='gray'), plt.title('scharr XY')


plt.show()