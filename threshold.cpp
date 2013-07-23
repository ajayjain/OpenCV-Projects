// Ajay Jain
// July 21, 2013
// threshold.cpp
// Threshold a color image from your webcam

#include <string>
#include <opencv2/opencv.hpp>

using namespace cv;

const string window = "Image Thresholding";

int main() {
  // Open and initailize camera
	VideoCapture cap(0);
	if (!cap.isOpened()) {
		printf("Couldn't open webcam \n");
		return -1;
	}

	// Create window and trackbars
	namedWindow(window);
	int thresholdValue, maxValue;
	createTrackbar("Threshold", window, &thresholdValue, 200);
	createTrackbar("Max Value", window, &maxValue, 200);
	
	Mat thresh;
	printf("Press any key to quit...\n");
	while (true) {
		cap >> thresh;
		cvtColor(thresh, thresh, CV_BGR2GRAY);
		Vec3b v = thresh.at<Vec3b>(0, 0);
		// printf("channels: %d, 0: %d, 1: %d, 2: %d\n", v.channels, v[0], v[1], v[2]);
		threshold(thresh, thresh, (double) thresholdValue, maxValue, THRESH_BINARY);
		imshow(window, thresh);
		if (waitKey(30) > 0) break;
	}

	return 0;
}
