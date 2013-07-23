// Ajay Jain
// July 19, 2013
// display.cpp
// Display image.

#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char** argv) {
  Mat image = imread(argv[1], 1);

  if(argc != 2 || !image.data) {
    printf("No image data. Usage: ./display path/to/image \n");
    return -1;
  }

  namedWindow("Display", CV_WINDOW_AUTOSIZE);
  imshow("Display", image);

  waitKey(0);

  return 0;
}
