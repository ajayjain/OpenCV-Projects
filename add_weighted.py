import cv2

logo = cv2.imread('img/opencv_logo.png')
im = cv2.imread('img/cards.png')
# im = cv2.imread('img/cards.png')[0:rows, 0:cols]

rows, cols, channels = logo.shape
smallim = cv2.resize(im, (cols, rows))
# cam = cv2.VideoCapture

print logo.shape
print smallim.shape

added = cv2.addWeighted(smallim, 0.8,	# alpha = 0.7
						logo, 0.2,	# beta  = 0.3
						0)			# gamma - scalar added to each sum

cv2.namedWindow('addWeighted')
cv2.imshow('addWeighted', added)
cv2.waitKey(0)
cv2.destroyAllWindows()