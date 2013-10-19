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
    clue15 = Clue(Board.ACROSS, Coordinate(0,0), "Opposite of masc.")
    clue16 = Clue(Board.ACROSS, Coordinate(0,0), "Arranged in rows and columns")
    clue18 = Clue(Board.ACROSS, Coordinate(0,0), "Promissory Note")
    clue20 = Clue(Board.ACROSS, Coordinate(0,0), "Coal Bed")
    clue21 = Clue(Board.ACROSS, Coordinate(0,0), "Make suitable")
    clue23 = Clue(Board.ACROSS, Coordinate(0,0), "Is concerned")
    clue27 = Clue(Board.ACROSS, Coordinate(0,0), "TV knob")
    clue28 = Clue(Board.ACROSS, Coordinate(0,0), "Magazine Stand")
    clue31 = Clue(Board.ACROSS, Coordinate(0,0), "Rescue Worker (abbr.)")
    clue32 = Clue(Board.ACROSS, Coordinate(0,0), "__ du Diable (Devil's Island)")
    clue33 = Clue(Board.ACROSS, Coordinate(0,0), "Campaign Workers")
    clue34 = Clue(Board.ACROSS, Coordinate(0,0), "Tell tales")
    clue35 = Clue(Board.ACROSS, Coordinate(0,0), "__ Plaines")
    clue36 = Clue(Board.ACROSS, Coordinate(0,0), "Mineral Vein")
    clue37 = Clue(Board.ACROSS, Coordinate(0,0), "Throw rocks at")
    clue38 = Clue(Board.ACROSS, Coordinate(0,0), "Ford lemon")
    clue40 = Clue(Board.ACROSS, Coordinate(0,0), "Certain NCO")
    clue42 = Clue(Board.ACROSS, Coordinate(0,0), "Salamander")
    clue45 = Clue(Board.ACROSS, Coordinate(0,0), "Teachers' gp.")
    clue46 = Clue(Board.ACROSS, Coordinate(0,0), "Stumbled")
    clue50 = Clue(Board.ACROSS, Coordinate(0,0), "Roof sealer")
    clue53 = Clue(Board.ACROSS, Coordinate(0,0), "Fortune")
    clue54 = Clue(Board.ACROSS, Coordinate(0,0), '"__ and Ivory"')
    clue55 = Clue(Board.ACROSS, Coordinate(0,0), "Make last")
    clue56 = Clue(Board.ACROSS, Coordinate(0,0), "Thanksgiving tuber")
    clue57 = Clue(Board.ACROSS, Coordinate(0,0), "Farewells")
    clue58 = Clue(Board.ACROSS, Coordinate(0,0), "U.S.A.'s 'Uncle'")

    clue1d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,3), "Lout")
    clue2d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,8), "Application")
    clue3d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Shyness")
    clue4d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,6), "Illuminated (2 wds.)")
    clue5d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,9), "Boise's state (abbr.)")
    clue6d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Throngs")
    clue7d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,2), '"__ Skies"')
    clue8d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Likely (to)")
    clue9d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Foot part")
    clue10d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Venerable")
    clue13d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Sports pants")
    clue17d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Medical gp.")
    clue19d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Certain grain")
    clue21d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Felt sick")
    clue22d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Half a sextet")
    clue24d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Banishes")
    clue25d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Novelist Zola")
    clue26d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Proofreading note")
    clue27d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Detergent brand")
    clue29d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Increase the number")
    clue30d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Passable grades")
    clue33d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Declare to be true")
    clue37d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Prior to (prefix)")
    clue39d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Liverpool's locale (abbr.)")
    clue41d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Griffith and Rooney")
    clue43d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), 'Jack of "Dragnet"')
    clue44d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Actor Donahue")
    clue46d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Tricky")
    clue47d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "One __ customer (2 wds.)")
    clue48d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Modern bank teller (abbr.)")
    clue49d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "WSW's opp.")
    clue51d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Alias initials")
    clue52d = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0,0), "Sleep stage (abbr.)")

    scraper.Scraper().run_scraper([clue1, clue4, clue8, clue11, clue12, clue14, clue15, clue16, clue18, clue20, clue21, clue23,
      clue27, clue28, clue31, clue32, clue33, clue34, clue35, clue36, clue37, clue38, clue40, clue42, clue45, clue46, clue50,
      clue53, clue54, clue55, clue56, clue57, clue58, clue1d, clue2d, clue4d, clue5d, clue6d, clue7d, clue8d, clue9d, clue10d,
      clue13d], self.b.board)
    #solver.Solver(self.b.board, [c1, c2]).solve()
    #self.produce_output()
    # scraper.Scraper().run_scraper([clue1, clue2, clue3, clue4], self.b.board)
    # clue1.word_list = ["out"]
    # clue4.word_list = ["limb"]
    # clue8.word_list = ["ato"]
    # clue11.word_list = ["asi"]
    # clue12.word_list = ["idols"]
    # clue14.word_list = ["pol"]
    # solver.Solver(self.b.board, [clue1, clue4, clue8, clue11, clue12, clue14]).solve()
    # self.produce_output()

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
