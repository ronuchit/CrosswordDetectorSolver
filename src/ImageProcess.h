#include <iostream>
#include <fstream>
#include "CImg/CImg.h"
using namespace std;
using namespace cimg_library;

class ImageProcess {
  private:
    int length;
    double blockSize;
    float numSamples;
    string imageName;

  public:
    ImageProcess();
    ImageProcess(int& length, double& blockSize);
    void cellDetect();
    
};
