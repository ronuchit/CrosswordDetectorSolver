#include <iostream>

class Test {
    public:
        int* bar(int x) {
          int* a;
          int b[] = {1, 2};
          a = b;
          return a;
        }
};

extern "C" {
  Test* Test_new() {
    return new Test();
  }
  int* Test_bar(Test* test, int x) {
    int* a = test->bar(x);
    std::cout << a[0] << "\n";
    std::cout << a[1] << "\n";
  }
}
