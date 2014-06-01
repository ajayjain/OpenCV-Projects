from __future__ import print_function
import numpy as np
import cv2
import random

FILENAME = "./img/cards.png"
WINDOW_NAME = "Cards"
NUMCARDS = 4

def centroid(moment):
	x = moment['m10'] // moment['m00']
	y = moment['m01'] // moment['m00']
	return (x, y)

def draw_centroid(c, im):
	max_rows = im.shape[0]
	max_cols = im.shape[1]
	for dx in xrange(-3, 3):
		for dy in xrange(-3, 3):
			x = c[0] + dx
			y = c[1] + dy
			if (x > 0 and y > 0 and y < max_rows and x < max_cols):
				im[y, x] = np.array([1, 1, 255])

# cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.namedWindow(WINDOW_NAME)

# im = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)

im = cv2.imread(FILENAME)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(imgray, (1, 1), 1000)
flag, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours.sort(key=cv2.contourArea, reverse=True) # cv2.contourArea is a lambda that
												 # calculates the area of a contour based a list element
												 # reverse=True: descending order (biggest first)
# contours = contours[:8] # 4 biggest cosntours (4 cards)

print("Contours: ", len(contours))

colorim = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

for contour in contours:
	cv2.drawContours(
					colorim,
					[contour],
					0,		# which contour to draw (-1 is all)
					# (255, 0, 0),
					(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),  # color (BGR)
					2	# thickness
				)

moments = map(cv2.moments, contours)
centroids = map(centroid, moments)
print(centroids[0])
print([colorim[centroid[0], centroid[1]] for centroid in centroids])
for centroid in centroids:
	draw_centroid(centroid, colorim)

cv2.imshow(WINDOW_NAME, colorim)
cv2.waitKey(0)
cv2.destroyAllWindows()

