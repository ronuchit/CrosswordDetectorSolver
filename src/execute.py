#! /usr/bin/python

import board
import scraper
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
    clue1 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(3,0), "Ump's call")
    clue4 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0,0), "Branch")
    clue8 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(6,12), "From __ Z (2 wds.)")
    clue11 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(8,0), '"__ was saying..." (2 wds.)')
    clue12 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0,5), "Teens' heroes")
    clue14 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(11,12), "Candidate, for short")
    # clue15 = Clue(Board.ACROSS, Coordinate(), "Opposite of masc.")
    # clue16 = Clue(Board.ACROSS, Coordinate(), "Arranged in rows and columns")
    # clue18 = Clue(Board.ACROSS, Coordinate(), "Promissory Note")

    # clue1d = Clue(Board.DOWN, Coordinate(), "Lout")
    # clue2d = Clue(Board.DOWN, Coordinate(), "Application")
    # clue3d = Clue(Board.DOWN, Coordinate(), "Shyness")
    # clue4d = Clue(Board.DOWN, Coordinate(), "Illuminated (2 wds.)")
    # clue5d = Clue(Board.DOWN, Coordinate(), "Boise's state (abbr.)")

    # scraper.Scraper().run_scraper([clue1, clue2, clue3, clue4], self.b.board)
    clue1.word_list = ["out"]
    clue4.word_list = ["limb"]
    clue8.word_list = ["ato"]
    clue11.word_list = ["asi"]
    clue12.word_list = ["idols"]
    clue14.word_list = ["pol"]
    solver.Solver(self.b.board, [clue1, clue4, clue8, clue11, clue12, clue14]).solve()
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
