#! /usr/bin/python

class Clue(object):
  def __init__(self, direction, coord, clue_str):
    self.direction = direction
    self.coord = coord
    self.clue_str = clue_str
    self.word_list = None

  def __repr__(self):
    return "coord: %s\nclue: %s"%(self.coord, self.clue_str)

