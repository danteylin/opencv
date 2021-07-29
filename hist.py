import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('SKADI.png', 0)
# 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
plt.plot(hist1)
img2 = cv2.imread('test6.jpg')
color = ('b', 'g', 'r')
#for i, col in enumerate(color):
histr = cv2.calcHist([img2], [0], None, [256], [0, 256])
plt.plot(histr)
plt.xlim([0, 256]), plt.title('Histogram')


plt.show()       