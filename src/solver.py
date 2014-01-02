#! /usr/bin/python

import board
import numpy as np
import copy

class IncompatibleLengthException(Exception):
  pass

class SolverFailedError(Exception):
  pass

class Solver(object):
  def __init__(self, b, clues):
    self.board_instance = b
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
      self._solve(self.board_instance.board)

  def _solve(self, curr_board):
    if len(self.longer_clues) > 0:
      clue = self.longer_clues[self.index]
      for word in clue.word_list:
        new_board = copy.deepcopy(curr_board)
        try:
          if self.place_letters(clue.coord.x, clue.coord.y, word, clue.direction, new_board): # complete solution found
            self.board_instance.board = new_board
            return True
        except board.InvalidLetterException:
          continue
        self.index += 1
        try:
          if self._solve(new_board):
            return True
        except SolverFailedError:
          pass
        self.index -= 1
        self.num_remaining += 1
    raise SolverFailedError("No solution found!")

  def fill_guarantees(self):
    for clue in self.clues:
      if len(clue.word_list) == 1:
        word = clue.word_list[0]
        c_x, c_y = clue.coord.x, clue.coord.y
        if clue.direction == board.Board.ACROSS:
          length = self.board_instance.board[c_x, c_y].right_length
        else:
          length = self.board_instance.board[c_x, c_y].down_length
          
        try:
          self.place_letters(c_x, c_y, word, clue.direction, self.board_instance.board)
        except board.InvalidLetterException:
          raise SolverFailedError("Found incompatible intersection when solving guarantees (this shouldn't happen)!")

  def place_letters(self, c_x, c_y, word, direction, curr_board):
    x, y = c_x, c_y
    old_letters = []
    for i in range(len(word)):
      try:
        old_letters.append(curr_board[x, y].letter)
        curr_board[x, y].set_letter(word[i])
      except board.InvalidLetterException as e:
        if direction == board.Board.DOWN:
          for corr_x in range(c_x, x):
            curr_board[corr_x, y].set_letter(old_letters[corr_x - c_x])
        else:
          for corr_y in range(c_y, y):
            curr_board[x, corr_y].set_letter(old_letters[corr_y - c_y])
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

if __name__ == "__main__":
  import clue, coordinate
  color_arr = np.array([[1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1]])
  b = board.Board(color_arr)
  b.construct_board()
  c1 = clue.Clue(board.Board.ACROSS, coordinate.Coordinate(0, 0), "whe1")
  c1.word_list = ["hey", "wey"]
  c2 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0, 0), "whe2")
  c2.word_list = ["gist", "hist"]
  c3 = clue.Clue(board.Board.DOWN, coordinate.Coordinate(0, 1), "whe3")
  c3.word_list = ["fein", "eins"]
  Solver(b, [c3, c2, c1]).solve()
  b.print_board()
