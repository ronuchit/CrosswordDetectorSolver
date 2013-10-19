#! /usr/bin/python

import board
import numpy as np

class IncompatibleLengthException(Exception):
  pass

class SolverFailedError(Exception):
  pass

class Solver(object):
  def __init__(self, board_repr, clues):
    self.board_repr = board_repr
    self.clues = clues
    self.longer_clues = []
    
  def solve(self):
    self.fill_guarantees()

  def fill_guarantees(self):
    for clue in self.clues:
      if len(clue.word_list) == 1:
        word = clue.word_list[0]
        c_x, c_y = clue.coord.x, clue.coord.y
        if clue.direction == board.Board.RIGHT:
          length = self.board_repr[c_x, c_y].right_length
        else:
          length = self.board_repr[c_x, c_y].down_length
          
        self.check_length_validity(length, word)
        x, y = c_x, c_y
        for i in range(len(word)):
          try:
            self.board_repr[x, y].set_letter(word[i])
          except board.InvalidLetterException:
            raise SolverFailedError("Found incompatible intersection when solving guarantees!")
          if clue.direction == board.Board.DOWN:
            x += 1
          else:
            y += 1
      else:
        self.longer_clues.append(clue)

  def check_length_validity(self, req_len, word):
    if req_len != len(word):
      raise IncompatibleLengthException("%s is not of length %d"%(word, req_len))

if __name__ == "__main__":
  import clue, coordinate
  color_arr = np.array([[1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1]])
  b = board.Board(color_arr)
  b.construct_board()
  c1 = clue.Clue(board.Board.RIGHT, coordinate.Coordinate(0, 0), "whe")
  c1.word_list = ["hey"]
  c2 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0, 0), "whe2")
  c2.word_list = ["gist"]
  Solver(b.board, [c1, c2]).solve()
  b.print_board()
