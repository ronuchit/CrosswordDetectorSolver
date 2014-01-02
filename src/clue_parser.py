#!/usr/bin/env python 
import clue
import re

def parse(board):
  with open('clues.txt', 'r') as f:
    temp = f.read()
    numbers = re.findall("\d*?\.", temp);
    clues = re.split("\d*?\.", temp);
  numbers = filter(lambda x : x != '.', numbers)
  clues = filter(lambda x : x != '', clues)
  clues2 = []
  for c in clues:
    c2 = c.rstrip('\n')
    i = 0
    while (i < len(c2)):
      if (c2[i] == '('):
        c2 = c2[0:i]
        break;
      elif (c2[i] == ')'):
        c2 = ' '
        break;
      i = i + 1
    if (len(c2)>1):
      clues2.append(c2)
  clues2 = clues2[1:]
  start_of_down = 0
  i = 0
  while (i < len(clues2)):
    if ("DOWN" in clues2[i]):
      start_of_down = i+1
      clues2 = clues2[0:start_of_down+1] + clues2[(start_of_down+1):]
      break
    i = i + 1
  # changeClues(numbers, clues2)
  return make_clues(clues2, numbers, start_of_down, board)

def changeClues(x,y):
  change = True;
  while(change == True):
    i = 0
    while (i < len(x)):
      print(str(x[i]) + y[i])
      i = i + 1
    answer = raw_input("Do you want to change anything?")
    if(answer.lower() == "yes"):
      index = raw_input("Which number do you want to change?")
      if(int(index) >= len(x)):
        print "invalid statement or not in range"
        continue;
      x[int(index)] = raw_input("Change to:?")
    else:
      print "no"
      change = False
      return x

def make_clues(str_list, num_list, down_start, board):
  num_list = map(lambda x: x[:-1], num_list)
  toReturn = []
  across_lst = [13, 19, 24, 30, 37, 41]
  down_lst = [6, 7, 8, 13, 16, 26, 27]
  for i in range(len(str_list)):
    if i < down_start and int(num_list[i]) in across_lst:
      toReturn.append(clue.Clue(board.ACROSS, board.numbers_dict[int(num_list[i])], str_list[i]))
    elif i >= down_start and int(num_list[i]) in down_lst:
      toReturn.append(clue.Clue(board.DOWN, board.numbers_dict[int(num_list[i])], str_list[i]))
  return toReturn

if __name__ == "__main__": 
  parse()
