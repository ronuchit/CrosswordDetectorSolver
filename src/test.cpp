#include <iostream>

class Test {
    public:
        void bar(int x) {
            std::cout << x << std::endl;
        }
};

extern "C" {
    Test* Test_new() {
      return new Test();
    }
  void Test_bar(Test* test, int x) {
      test->bar(x);
    }
}
