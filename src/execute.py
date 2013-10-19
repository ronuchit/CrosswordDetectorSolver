#! /usr/bin/python

<<<<<<< Updated upstream
import board
import scraper
import solver
import clue
import coordinate
=======
from board import *
from scraper import *
from solver import *
from clue import *
from coordinate import *
>>>>>>> Stashed changes
import numpy as np
from math import sqrt

class Executor(object):
  def __init__(self):
    self.color_array = self.create_color_array()
    self.b = board.Board(self.color_array)

  def execute(self):
<<<<<<< Updated upstream
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

    scraper.Scraper().run_scraper([clue1, clue2, clue3, clue4], self.b.board)
=======
    clue1 = Clue(Board.ACROSS, Coordinate(3,0), "Ump's call")
    clue4 = Clue(Board.ACROSS, Coordinate(0,0), "Branch")
    clue8 = Clue(Board.ACROSS, Coordinate(6,12), "From __ Z (2 wds.)")
    clue11 = Clue(Board.ACROSS, Coordinate(8,0), '"__ was saying..." (2 wds.)')
    clue12 = Clue(Board.ACROSS, Coordinate(0,5), "Teens' heroes")
    clue14 = Clue(Board.ACROSS, Coordinate(), "Candidate, for short")
    clue15 = Clue(Board.ACROSS, Coordinate(), "Opposite of masc.")
    clue16 = Clue(Board.ACROSS, Coordinate(), "Arranged in rows and columns")
    clue18 = Clue(Board.ACROSS, Coordinate(), "Promissory Note")

    clue1d = Clue(Board.DOWN, Coordinate(), "Lout")
    clue2d = Clue(Board.DOWN, Coordinate(), "Application")
    clue3d = Clue(Board.DOWN, Coordinate(), "Shyness")
    clue4d = Clue(Board.DOWN, Coordinate(), "Illuminated (2 wds.)")
    clue5d = Clue(Board.DOWN, Coordinate(), "Boise's state (abbr.)")

    Scraper().run_scraper([clue1, clue2, clue3, clue4], self.b.board)
>>>>>>> Stashed changes
    #solver.Solver(self.b.board, [c1, c2]).solve()
    #self.produce_output()

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
  
if __name__ == "__main__":
  Executor().execute()
