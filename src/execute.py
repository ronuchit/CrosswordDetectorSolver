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
    # clue1 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,10), "Hawaiian souvenir")
    # clue2 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,11), "Chicago trains")
    # clue3 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(1,9), "Soccer legend")
    # clue4 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(2,8), "Circle segment")
    # clue5 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(1,9), "Implore")
    # clue6 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(3,7), "Mine find")
    # clue7 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(4, 8), '"Cheers" waitress')
    # clue8 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(5, 9), "Regard")
    # clue9 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,11), "Renting contract")
    # clue10 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,7), "Toast topping")
    # clue11 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,12), "Stockpile")
    # clue12 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(7,5), "Simplicity")
    # clue13 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(8,6), "Settings")
    # clues = [clue3, clue1, clue2, clue4, clue5, clue6, clue7, clue8, clue9, clue10, clue11, clue12, clue13]
    clues = clue_parser.parse(self.b)
    clues = [clues[0], clues[7], clues[8], clues[10], clues[9], clues[1], clues[2], clues[3], clues[11], clues[6], clues[12], clues[4], clues[5]]
    
    scraper.Scraper().run_scraper(clues, self.b.board)
    solver.Solver(self.b.board, clues).solve()
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
