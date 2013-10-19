#! /usr/bin/python

# Internal representation of the board, as a 2D array of Blocks.

import numpy as np

BLACK = 0
WHITE = 1
RIGHT = 0
DOWN = 1

class Board(object):
  def __init__(self, color_arr):
    self.color_arr = color_arr
    self.side_length = np.shape(self.color_arr)[0]
    self.construct_board()
    self.print_board()

  def construct_board(self):
    # creates self.board and self.numbers_dict (key: number, value: Coordinate object)
    board = np.empty((self.side_length, self.side_length), dtype=Block)
    curr_num = 1
    numbers_dict = {}
    
    for row in range(self.side_length):
      for column in range(self.side_length):
        if color_arr[row, column] == BLACK:
          board[row, column] = Block(BLACK, right_length=None, down_length=None)
        elif (row == 0 and column == 0) or \
              (board[row-1, column] is not None and \
                 board[row-1, column].color == BLACK and \
                 board[row, column-1] is not None and \
                 board[row, column-1].color == BLACK):
          numbers_dict[curr_num] = Coordinate(row, column)
          curr_num += 1
          board[row, column] = self._construct_beginning_block(row, column, do_right=True, do_down=True)
        elif row == 0 or board[row-1, column].color == BLACK:
          numbers_dict[curr_num] = Coordinate(row, column)
          curr_num += 1
          board[row, column] = self._construct_beginning_block(row, column, do_right=False, do_down=True)
        elif column == 0 or board[row, column-1].color == BLACK:
          numbers_dict[curr_num] = Coordinate(row, column)
          curr_num += 1
          board[row, column] = self._construct_beginning_block(row, column, do_right=True, do_down=False)
        else:
          board[row, column] = Block(self.color_arr[row, column], right_length=None, down_length=None)
          
    self.board = board
    self.numbers_dict = numbers_dict

  def print_board(self):
    print("numbers_dict:")
    for num, coord in self.numbers_dict.items():
      print("num: %s; coord: %s"%(num, coord))
    print("\n\n\nboard:")
    for row in range(self.side_length):
      for column in range(self.side_length):
        print("row: %d; column: %d"%(row, column))
        print(self.board[row, column])
        print
          
  def _construct_beginning_block(self, row, column, do_right, do_down):
    if do_right:
      right_length = 0
      count = column
      while count < self.side_length and self.color_arr[row, count] == WHITE:
        count += 1;
        right_length += 1;
    else:
      right_length = None

    if do_down:
      down_length = 0
      count = row
      while count < self.side_length and self.color_arr[count, column] == WHITE:
        count += 1;
        down_length += 1;
    else:
      down_length = None
      
    return Block(self.color_arr[row, column], right_length=right_length, down_length=down_length)


class Block(object):
  def __init__(self, color, right_length=None, down_length=None):
    self.color = color
    self.right_length = right_length
    self.down_length = down_length
    self.letter = None
              
  def __repr__(self):
    return "color: %s; right_length: %s; down_length: %s"%(self.color, str(self.right_length), str(self.down_length))

class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "(x, y) = (%d, %d)"%(self.x, self.y)

if __name__ == "__main__":
  color_arr = np.array([[1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 1, 1]])
  Board(color_arr).construct_board()
