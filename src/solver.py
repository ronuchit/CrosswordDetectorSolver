#! /usr/bin/python

import board
import numpy as np
import sys

class IncompatibleLengthException(Exception):
  pass

class SolverFailedError(Exception):
  pass

class Solver(object):
  def __init__(self, board_repr, clues):
    self.board_repr = board_repr
    self.clues = clues
    self.longer_clues = []
    self.num_remaining = len(self.clues)
    for c in self.clues:
      if len(c.word_list) > 1:
        self.longer_clues.append(c)
      elif len(c.word_list) == 0:
        print("No answers for clue %s; ignoring"%c.clue_str)
        self.num_remaining -= 1
    
  def solve(self):
    self.fill_guarantees()
    if len(self.longer_clues) > 0:
      self._solve()

  def _solve(self, words=[]):
    if len(self.longer_clues) > 0:
      clue = self.longer_clues[0]
      for word in clue.word_list:
        try:
          if self.place_letters(clue.coord.x, clue.coord.y, word, clue.direction):
            return True          
        except board.InvalidLetterException:
          continue
        del self.longer_clues[0]
        try:
          if self._solve(words+[word]):
            return True
        except SolverFailedError:
          pass
        self.longer_clues.insert(0, clue)
        self.unplace_letters(clue.coord.x, clue.coord.y, word, clue.direction)
    raise SolverFailedError("No solution found!")

  def fill_guarantees(self):
    for clue in self.clues:
      if len(clue.word_list) == 1:
        word = clue.word_list[0]
        c_x, c_y = clue.coord.x, clue.coord.y
        if clue.direction == board.Board.ACROSS:
          length = self.board_repr[c_x, c_y].right_length
        else:
          length = self.board_repr[c_x, c_y].down_length
          
        self.check_length_validity(length, word)
        try:
          if self.place_letters(c_x, c_y, word, clue.direction):
            return
        except board.InvalidLetterException:
          raise SolverFailedError("Found incompatible intersection when solving guarantees (this shouldn't happen)!")

  def place_letters(self, c_x, c_y, word, direction):
    x, y = c_x, c_y
    for i in range(len(word)):
      self.board_repr[x, y].set_letter(word[i])
      if direction == board.Board.DOWN:
        x += 1
      else:
        y += 1
    self.num_remaining -= 1
    if self.num_remaining == 0:
      print("Solution found!")
      return True
    return False

  def unplace_letters(self, c_x, c_y, word, direction):
    x, y = c_x, c_y
    for i in range(len(word)):
      self.board_repr[x, y].set_letter(self.board_repr[x, y].prev_letter)
      if direction == board.Board.DOWN:
        x += 1
      else:
        y += 1
    self.num_remaining += 1

  def check_length_validity(self, req_len, word):
    if req_len != len(word):
      raise IncompatibleLengthException("%s is not of length %d"%(word, req_len))

if __name__ == "__main__":
  import clue, coordinate
  color_arr = np.array([[1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1]])
  b = board.Board(color_arr)
  b.construct_board()
  c1 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0, 0), "whe")
  c1.word_list = ["hey"]
  c2 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0, 0), "whe2")
  c2.word_list = ["gist"]
  Solver(b.board, [c1, c2]).solve()
  b.print_board()
