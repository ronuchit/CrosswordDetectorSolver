#! /usr/bin/python

import board
import scraper
import clue_parser
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
    clues = clue_parser.parse(self.b)
    
    scraper.Scraper().run_scraper(clues, self.b.board)
    print("Solving puzzle...")
    solver.Solver(self.b, clues).solve()
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
    with open("../temp/solution_info.txt", "w+") as f:
      for row in range(side_length):
        for column in range(side_length):
          if self.b.board[row, column].color == board.Board.BLACK:
            f.write("black %s %s\n"%(row, column))
          else:
            f.write("%s %s %s\n"%(str(self.b.board[row, column].letter), row, column))
    with open("../temp/numbers_info.txt", "w+") as f:
      for num, coord in self.b.numbers_dict.items():
        f.write("%s %s %s\n"%(num, coord.x, coord.y))
  
if __name__ == "__main__":
  Executor().execute()
