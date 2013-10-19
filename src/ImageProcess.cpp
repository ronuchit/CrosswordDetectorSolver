#include "ImageProcess.h"

#define MAX_R 150
#define MAX_G 150 
#define MAX_B 150
#define MIN_W 10
#define MIN_H 10
#define X_INC 45
#define Y_INC 45
#define X_BOX_INC 5
#define Y_BOX_INC 5

ImageProcess::ImageProcess() {
  this->numSamples = (X_INC * Y_INC) / (X_BOX_INC * Y_BOX_INC);
}

ImageProcess::ImageProcess(int& length, double& blockSize) {
  this->length = length;
  this->blockSize = blockSize;
  this->numSamples = (X_INC * Y_INC) / (X_BOX_INC * Y_BOX_INC);
}

int main() {
  int length = 13;
  double blockSize = 45;
  ImageProcess ip = ImageProcess(length, blockSize);
  ip.cellDetect();
}

void ImageProcess::cellDetect() {
  CImg<unsigned char> src("../images/test1.jpg");
  src.blur(15);
  int y = 0;
  ofstream myFile;
  int width = src.width();
  int height = src.height();
  myFile.open("color_info.txt");
  // loop through each supposed "BOX"
  for(int j = MIN_H; j < height; j+=Y_INC) {
    int x = 0;
    for(int i = MIN_W; i < width; i+=X_INC) {
      int r = 0;
      int g = 0;
      int b = 0;
      // loop through a box and determine the average of colors along a portion of 
      // width and height
      for(int l = 0; l < Y_INC; l += Y_BOX_INC) {
        for(int k = 0; k < X_INC; k += X_BOX_INC ) {
          // 0 1 2 correspond to RGB colors in () operators
          r += src(i + l, j + k, 0, 0);
          g += src(i + l, j + k, 0, 1);
          b += src(i + l, j + k, 0, 2);
        }
      }
      float rAvg = r / numSamples;
      float gAvg = g / numSamples;
      float bAvg = b / numSamples;
      if (rAvg < MAX_R && gAvg < MAX_G && bAvg < MAX_B) {
        myFile << y << " " << x << " " << 0 << endl;
      } else {
        myFile << y << " " << x << " " << 1 << endl;
      }
      x++;
    }
    y++;
  }
  myFile.close();
}
