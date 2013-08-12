// Ajay Jain
// July 19, 2013
// haar-face-detect.cpp
// Detect faces with OpenCV

#include <string>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;

#ifdef __APPLE__
  string cascade_file = "/opt/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml";
#else
	string cascade_file = "C:/Users/Ajay/Code/ComputerVision/opencv/data/haarcascades/haarcascade_frontalface_default.xml";
	//string cascade_file = "C:/Users/Ajay/Code/ComputerVision/opencv/data/haarcascades/haarcascade_mcs_eyepair_big.xml";
//string cascade_file = "C:/Users/Ajay/Code/ComputerVision/opencv/data/haarcascades/haarcascade_mcs_profileface.xml";
#endif

const string window = "Face Detection";
CascadeClassifier cascade;

Mat eyeOrig = imread("C:/Users/Ajay/Documents/Visual Studio 2013/Projects/images/eye.png");

void overlayImage(Mat src, Mat overlay, int x, int y, Scalar S = Scalar(0,0,0,0), Scalar D = Scalar(1,1,1,1)) {
	#ifdef afsd
	for (int i = location.y; i < (location.y + overlay.cols); i++) {
		for (int j = location.x; j < (location.x + overlay.rows); j++) {
			Scalar source = src.at<float>(i, j);
			Scalar over = overlay.at<float>(i - location.y, j - location.x);

			for (int i = 0; i < 4; i++)
				src.at<float>(i + location.y, j + location.x, i) = (S.val[i] * source.val[i] + D.val[i] * over.val[i]);
		}
	}
	
	std::cout << ", Channels: " << src.channels() << std::endl;
	for (int r = y; r < (y + overlay.rows); r++) {
		uchar* srow = src.ptr(r);	// source row
		uchar* orow = overlay.ptr(r);	// overlay row
		for (int c = x; c < (x + overlay.cols); c++) {
			srow[c] = orow[c - x];
			//printf("(row: %d, col: %d, val: %d", r, c, row[c]);
		}
		//printf("\n\n");
	}
	#endif
}

void detectFaces(Mat &input, Mat &output) {
	cvtColor(input, output, CV_BGR2GRAY);
	equalizeHist(output, output);

	vector<Rect> objects;
	cascade.detectMultiScale(output, objects);

	printf("\n======================================\n");

	for (Rect r : objects) {
		printf("x: %d, y: %d, width: %d, height: %d \n", r.x, r.y, r.width, r.height);
		rectangle(input, r, Scalar(0, 0, 255), 3);

		//Mat eye;
		//resize(eyeOrig, eye, output.size());
		//eye.resize(output.rows);
		//add(output, eye, output);
	}
}

int main(int argc, char** argv) {
	if (argc > 1)
		cascade_file = argv[1];
	// Load Haar cascade
	if (!cascade.load(cascade_file)) {
		std::cerr << "Couldn't load cascade \"" << cascade_file << "\" \n"
			<< "Usage: ./haardetect --cascade path/to/haarcascade_frontalface_alt.xml" << std::endl;
		return -1;
	}

	// Open and initailize camera
	VideoCapture cap(0);
	if (!cap.isOpened()) {
		printf("Couldn't open webcam \n");
		return -1;
	}

	Mat faces;

	// show eye
	//namedWindow("eye", 1);
	//imshow("eye", eyeOrig);

	namedWindow(window, 1);
	while (true) {
		Mat frame;
		cap >> frame;

		if (!frame.data) {
			printf("No frame data \n");
			return -1;
		}
		
		detectFaces(frame, faces);
		std::cout << "Frame type: " << frame.type() << "\n";
		//overlayImage(frame, eye, 0, 0);

		//std::cout << "Frame dimen: " << fize.height << "\n";
		//eye.resize();
		//add(frame, eye, frame);

		imshow(window, frame);
		if (waitKey(30) >= 0) break;
	}

	return 0;
}
