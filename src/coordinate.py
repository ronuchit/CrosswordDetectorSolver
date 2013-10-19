#! /usr/bin/python

class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "(%d, %d)"%(self.x, self.y)
