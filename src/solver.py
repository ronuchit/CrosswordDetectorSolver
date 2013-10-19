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
    self.index = 0
    
  def solve(self):
    self.fill_guarantees()
    if len(self.longer_clues) > 0:
      self._solve()

  def _solve(self, words=[]):
    if len(self.longer_clues) > 0:
      clue = self.longer_clues[self.index]
      for word in clue.word_list:
        try:
          if self.place_letters(clue.coord.x, clue.coord.y, word, clue.direction):
            return True
        except board.InvalidLetterException:
          continue
        self.index += 1
        try:
          if self._solve(words+[word]):
            return True
        except SolverFailedError:
          pass
        self.index -= 1
        self.unplace_letters(clue.coord.x, clue.coord.y, word, clue.direction, words)
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
    old_letters = []
    for i in range(len(word)):
      try:
        old_letters.append(self.board_repr[x, y].letter)
        self.board_repr[x, y].set_letter(word[i])
      except board.InvalidLetterException as e:
        if direction == board.Board.DOWN:
          for corr_x in range(c_x, x):
            self.board_repr[corr_x, y].set_letter(old_letters[corr_x - c_x])
        else:
          for corr_y in range(c_y, y):
            self.board_repr[x, corr_y].set_letter(old_letters[corr_y - c_y])
        raise e
      if direction == board.Board.DOWN:
        x += 1
      else:
        y += 1
    self.num_remaining -= 1
    if self.num_remaining == 0:
      print("Solution found!")
      return True
    return False

  def unplace_letters(self, c_x, c_y, word, direction, words):
    x, y = c_x, c_y
    for i in range(len(word)):
      if direction == board.Board.DOWN:
        if (y == 0 or self.board_repr[x, y-1].letter is None) and (y == np.shape(self.board_repr)[0] - 1 or self.board_repr[x, y+1].letter is None):
          self.board_repr[x, y].set_letter(None)
        x += 1
      else:
        if (x == 0 or self.board_repr[x-1, y].letter is None) and (x == np.shape(self.board_repr)[0] - 1 or self.board_repr[x+1, y].letter is None):
          self.board_repr[x, y].set_letter(None)
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
