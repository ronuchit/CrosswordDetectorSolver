#include "ImageProcess.h"
#include <vector>

#define MAX_R 150
#define MAX_G 150 
#define MAX_B 150
#define MIN_R 100
#define MIN_G 100
#define MIN_B 100
#define Y_BOX_INC 5
#define X_BOX_INC 5

ImageProcess::ImageProcess() {
}

int main() {
  ImageProcess ip = ImageProcess();
  ip.readFile();
  ip.preprocess();
}

void ImageProcess::readFile() {
  string fname = "../temp/puzzle_info.txt";
  ifstream infile;
  string temp;
  infile.open(fname.c_str());
  getline(infile, temp);
  setImageName(temp.c_str());
  getline(infile, temp);
  setNumBlocks(atoi(temp.c_str()));
}

void ImageProcess::preprocess() {
  CImg<unsigned char> src(getImageName().c_str());
  int r = 0;
  int g = 0;
  int b = 0;
  // unneeded for now
  //int r_prev = 0;
  //int g_prev = 0;
  //int b_prev = 0;
  cimg_forXY(src, i, j) {
    //r_prev = r;
    //g_prev = g;
    //b_prev = b;
    r = src(i, j, 0, 0);
    g = src(i, j, 0, 1);
    b = src(i, j, 0, 2);
    if (r < MIN_R && g < MIN_G && b < MIN_B) {
      src(i, j, 0) = 0;
      src(i, j, 1) = 0;
      src(i, j, 2) = 0;
    } else {
      src(i, j, 0) = 255;
      src(i, j, 1) = 255;
      src(i, j, 2) = 255;
    }
  }
  src.blur(10);
  /* TESTING PURPOSES 
  CImgDisplay main_disp(src);
  while (!main_disp.is_closed()) 
    main_disp.wait();
  */
  int y = 0;
  ofstream myFile;
  int width = src.width();
  int height = src.height();
  myFile.open("../temp/color_info.txt");
  double blockPixels = width / getNumBlocks();
  double min_h = blockPixels / 4;
  double min_w = blockPixels / 4;
  // loop through each supposed "BOX"
  int numblacksquares = 0;
  float numSamples = 9;
  for(int j = min_h; j < height; j+=blockPixels) {
    int x = 0;
    for(int i = min_w; i < width; i+=blockPixels) {
      int r = 0;
      int g = 0;
      int b = 0;
      for(int l = 0; l <= (blockPixels / 2); l += (blockPixels / 4)) {
        for(int k = 0; k <= (blockPixels / 2); k += (blockPixels / 4)) {
          r += src(i + l, j + k, 0, 0);
          g += src(i + l, j + k, 0, 1);
          b += src(i + l, j + k, 0, 2);
        }
      }
      float rAvg = r / numSamples;
      float gAvg = g / numSamples;
      float bAvg = b / numSamples;
      if (rAvg < 100) {
        numblacksquares++;
        myFile << y << " " << x << " " << 0 << endl;
      } else {
        myFile << y << " " << x << " " << 1 << endl;
      }
      x++;
    }
    y++;
  }
  myFile.close();
  cout << numblacksquares;
}

void ImageProcess::cellDetect() {
  string srcName = getImageName();
  CImg<unsigned char> src(srcName.c_str());
  int y = 0;
  ofstream myFile;
  int width = src.width();
  int height = src.height();
  myFile.open("../temp/color_info.txt");
  double blockPixels = width / getNumBlocks();
  double min_h = blockPixels / 4;
  double min_w = blockPixels / 4;
  // loop through each supposed "BOX"
  int numblacksquares = 0;
  float numSamples = 9;
  for(int j = min_h; j < height; j+=blockPixels) {
    int x = 0;
    for(int i = min_w; i < width; i+=blockPixels) {
      int r = 0;
      int g = 0;
      int b = 0;
      for(int l = 0; l <= (blockPixels / 2); l += (blockPixels / 4)) {
        for(int k = 0; k <= (blockPixels / 2); k += (blockPixels / 4)) {
          r += src(i + l, j + k, 0, 0);
          g += src(i + l, j + k, 0, 1);
          b += src(i + l, j + k, 0, 2);
        }
      }
      float rAvg = r / numSamples;
      float gAvg = g / numSamples;
      float bAvg = b / numSamples;
      if (rAvg < 100) {
        numblacksquares++;
        myFile << y << " " << x << " " << 0 << endl;
      } else {
        myFile << y << " " << x << " " << 1 << endl;
      }
      x++;
    }
    y++;
  }
  myFile.close();
  cout << numblacksquares << endl;
}

string ImageProcess::getImageName() {
  return this->imageName;
}

void ImageProcess::setImageName(string imageName) {
  this->imageName = imageName;
}

int ImageProcess::getNumBlocks() {
  return this->numBlocks;
}

void ImageProcess::setNumBlocks(int numBlocks) {
  this->numBlocks = numBlocks;
}
