#! /usr/bin/python

import board
# import scraper
import solver
import numpy as np
from math import sqrt

class Executor(object):
  def __init__(self):
    self.color_array = self.create_color_array()
    
  def create_color_array(self):
    with open("color_info.txt", "r+") as f:
      lines = f.readlines()
    color_array = np.array([sqrt(len(lines)), sqrt(len(lines))], dtype=int)
    for line in lines:
      row, column, color = line.split
      color_array[int(row), int(column)] = color

  def execute(self):
    b = board.Board(color).construct_board()
    
    

if __name__ == "__main__":
  Executor().execute()
