from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
  def __init__(self):
    self.obj = lib.Test_new()
  def bar(self):
    return lib.Test_bar(self.obj, 5)

if __name__ == "__main__":
  f = Foo()
  print(f.bar())
