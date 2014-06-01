# import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/cards.png', cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
adaptive_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,15) # mean of 3 x 3
adaptive_gaussian = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,15) # weighted mean

cv2.imwrite('img/cards_threshold_binary.png', thresh1)
cv2.imwrite('img/cards_adaptive_threshold_mean.png', adaptive_mean)
cv2.imwrite('img/cards_adaptive_threshold_gaussian.png', adaptive_gaussian)

thresh = ['img','thresh1','thresh2','thresh3','thresh4','thresh5', 'adaptive_mean', 'adaptive_gaussian']

for i in xrange(8):
	plt.subplot(2,4,i+1)
	plt.imshow(eval(thresh[i]),'gray')
	plt.title(thresh[i])

plt.show()
# cv2.waitKey(0)
# sys.exit()