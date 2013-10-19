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
    clue1 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0,0), "Ump's call")
    clue4 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0,4), "Branch")
    clue8 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0,10), "From __ Z (2 wds.)")
    # clue11 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(1,0), '"__ was saying..." (2 wds.)')
    # clue12 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(1,4), "Teens' heroes")
    # clue14 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(1,10), "Candidate, for short")
    clue15 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(2,0), "Opposite of masc.")
    # clue16 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(2,4), "Arranged in rows and columns")
    # clue18 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(3,2), "Promissory Note")
    # clue20 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(3,6), "Coal Bed")
    # clue21 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(4,1), "Make suitable")
    # clue23 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(4,8), "Is concerned")
    # clue27 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(5,0), "TV knob")
    # clue28 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(5,5), "Magazine Stand")
    # clue31 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(5,10), "Rescue Worker (abbr.)")
    # clue32 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(6,0), "__ du Diable (Devil's Island)")
    # clue33 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(6,4), "Campaign Workers")
    # clue34 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(6,10), "Tell tales")
    # clue35 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(7,0), "__ Plaines")
    # clue36 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(7,4), "Mineral Vein")
    # clue37 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(7,9), "Throw rocks at")
    # clue38 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(8,0), "Ford lemon")
    # clue40 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(8,7), "Certain NCO")
    # clue42 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(9,3), "Salamander")
    # clue45 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(9,8), "Teachers' gp.")
    # clue46 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(10,0), "Stumbled")
    # clue50 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(10,10), "Roof sealer")
    # clue53 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(11,0), "Fortune")
    # clue54 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(11,4), '"__ and Ivory"')
    # clue55 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(11,10), "Make last")
    # clue56 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(12,0), "Thanksgiving tuber")
    # clue57 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(12,5), "Farewells")
    # clue58 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(12,10), "U.S.A.'s 'Uncle'")

    clue1d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Lout")
    clue2d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,1), "Application")
    clue3d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,2), "Shyness")
    # clue4d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,4), "Illuminated (2 wds.)")
    # clue5d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,5), "Boise's state (abbr.)")
    # clue6d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,6), "Throngs")
    # clue7d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,7), '"__ Skies"')
    # clue8d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,10), "Likely (to)")
    # clue9d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,11), "Foot part")
    # clue10d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,12), "Venerable")
    # clue13d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(1,8), "Sports pants")
    # clue17d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(2,9), "Medical gp.")
    # clue19d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(3,3), "Certain grain")
    # clue21d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,1), "Felt sick")
    # clue22d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,5), "Half a sextet")
    # clue24d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,10), "Banishes")
    # clue25d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,11), "Novelist Zola")
    # clue26d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(4,12), "Proofreading note")
    # clue27d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(5,0), "Detergent brand")
    # clue29d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(5,6), "Increase the number")
    # clue30d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(5,7), "Passable grades")
    # clue33d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(6,4), "Declare to be true")
    # clue37d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(6,10), "Prior to (prefix)")
    # clue39d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(7,3), "Liverpool's locale (abbr.)")
    # clue41d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(7,8), "Griffith and Rooney")
    # clue43d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(8,5), 'Jack of "Dragnet"')
    # clue44d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(8,6), "Actor Donahue")
    # clue46d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(9,0), "Tricky")
    # clue47d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(9,1), "One __ customer (2 wds.)")
    # clue48d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(9,2), "Modern bank teller (abbr.)")
    # clue49d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(9,7), "WSW's opp.")
    # clue51d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(9,11), "Alias initials")
    # clue52d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(9,12), "Sleep stage (abbr.)")

    # clues = [clue1, clue4, clue8, clue11, clue12, clue14, clue15, clue16, clue18, clue20, clue21, clue23,
    #   clue27, clue28, clue31, clue32, clue33, clue34, clue35, clue36, clue37, clue38, clue40, clue42, clue45, clue46, clue50,
    #   clue53, clue54, clue55, clue56, clue57, clue58, clue1d, clue2d, clue4d, clue5d, clue6d, clue7d, clue8d, clue9d, clue10d,
    #   clue13d]
    clues = [clue1, clue4, clue8, clue15, clue1d, clue2d, clue3d]
    scraper.Scraper().run_scraper(clues, self.b.board)
    #solver.Solver(self.b.board, [c1, c2]).solve()
    #self.produce_output()
    # scraper.Scraper().run_scraper([clue1, clue2, clue3, clue4], self.b.board)
    # clue1.word_list = ["out"]
    # clue4.word_list = ["limb"]
    # clue8.word_list = ["ato"]
    # clue11.word_list = ["asi"]
    # clue12.word_list = ["idols"]
    # clue14.word_list = ["pol"]
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
