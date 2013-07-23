// Ajay Jain
// July 19, 2013
// edges.cpp
// Finds edges from webcam video with adjustable blur size (ie noise reduction).

#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;

string window = "Edges";
string trackbar = "ksize";

void extractEdges(Mat &input, Mat &output) {
  cvtColor(input, output, CV_BGR2GRAY);

  int ksize = getTrackbarPos(trackbar, window)*2+1;
  GaussianBlur(output, output, Size(ksize, ksize), 1.5, 1.5);
  
  Canny(output, output, 0, 30, 3);
}

int main(int argc, char** argv) {
  // Open and initailize camera
  VideoCapture cap(0);
  if (!cap.isOpened()) {
    printf("Couldn't open webcam \n");
    return -1;
  }

  Mat edges;
  namedWindow(window, 1);
  createTrackbar(trackbar, window, NULL, 10);

  while (true) {
    Mat frame;
    cap >> frame;
    
    if(!frame.data) {
      printf("No frame data \n");
      return -1;
    }

    extractEdges(frame, edges);
    
    imshow(window, edges);

    if(waitKey(30) >= 0) break;
  }

  return 0;
}
