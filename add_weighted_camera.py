import cv2

logo = cv2.imread('img/opencv_logo.png')
rows, cols, channels = logo.shape

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
shape = frame.shape[:2][::-1]
logo = cv2.resize(logo, shape)

cv2.namedWindow('addWeighted')

while True:
	added = cv2.addWeighted(frame, 0.8,	# alpha = 0.7
							logo, 0.2,	# beta  = 0.3
							0)			# gamma - scalar added to each sum

	cv2.imshow('addWeighted', added)
	ret, frame = cap.read()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cap.release()
cv2.destroyAllWindows()