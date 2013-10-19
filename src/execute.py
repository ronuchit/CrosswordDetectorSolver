#! /usr/bin/python

import board
# import scraper
import solver
import clue
import coordinate
import numpy as np
from math import sqrt

class Executor(object):
  def __init__(self):
    self.color_array = self.create_color_array()
    self.b = board.Board(self.color_array)

  def execute(self):
    c1 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0, 0), "whe")
    c1.word_list = ["heys"]
    c2 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(7, 4), "whe2")
    c2.word_list = ["listen"]
    solver.Solver(self.b.board, [c1, c2]).solve()
    self.produce_output()

  def create_color_array(self):
    with open("../temp/color_info.txt", "r+") as f:
      lines = f.readlines()
    color_array = np.empty([sqrt(len(lines)), sqrt(len(lines))], dtype=int)
    for line in lines:
      row, column, color = line.split()
      color_array[int(row), int(column)] = color
      
    return color_array

  def produce_output(self):
    side_length = len(self.b.board)
    with open("solution_info.txt", "w+") as f:
      for row in range(side_length):
        for column in range(side_length):
          f.write("%s %s %s\n"%(str(self.b.board[row, column].letter), row, column))
  
if __name__ == "__main__":
  Executor().execute()
