#include <iostream>
#include <fstream>
#include "CImg/CImg.h"
using namespace std;
using namespace cimg_library;

class ImageProcess {
  private:
    int numBlocks;
    string imageName;

  public:
    ImageProcess();
    void readFile();
    void preprocess();
    void cellDetect();
    string getImageName();
    void setImageName(string imageName);
    int getNumBlocks();
    void setNumBlocks(int numBlocks);
};
