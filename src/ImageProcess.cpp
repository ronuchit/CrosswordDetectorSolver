#include "ImageProcess.h"
#include <vector>

#define MAX_R 150
#define MAX_G 150 
#define MAX_B 150

ImageProcess::ImageProcess() {
}

int main() {
  ImageProcess ip = ImageProcess();
  ip.readFile();
  ip.cellDetect();
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
CImg<unsigned char> src("../images/photo.jpg");
  int r = 0;
  int g = 0;
  int b = 0;
  cimg_forXY(src, i, j) {
    r = src(i, j, 0, 0);
    g = src(i, j, 0, 1);
    b = src(i, j, 0, 2);
    if (r < MAX_R && g < MAX_G && b < MAX_B) {
      src(i, j, 0) = 0;
      src(i, j, 1) = 0;
      src(i, j, 2) = 0;
    } else {
      src(i, j, 0) = 255;
      src(i, j, 1) = 255;
      src(i, j, 2) = 255;
    }
  }
  CImgDisplay main_disp(src);
  while (!main_disp.is_closed()) 
    main_disp.wait();
  src.save_bmp("test.bmp");
}

void ImageProcess::cellDetect() {
  string srcName = getImageName();
  CImg<unsigned char> src(srcName.c_str());
  src.blur(15);
  int y = 0;
  ofstream myFile;
  int width = src.width();
  int height = src.height();
  myFile.open("../temp/color_info.txt");
  double blockPixels = width / getNumBlocks();
  double min_h = blockPixels / 2;
  double min_w = blockPixels / 2;
  // loop through each supposed "BOX"
  int numblacksquares = 0;
  for(int j = min_h; j < height; j+=blockPixels) {
    int x = 0;
    for(int i = min_w; i < width; i+=blockPixels) {
      int r = src(i, j, 0, 0);
      int g = src(i, j, 0, 1);
      int b = src(i, j, 0, 2);
      if (r < MAX_R && g < MAX_G && b < MAX_B) {
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
