#!/usr/bin/env python 
import clue
import re

def parse():
  with open('clues.txt', 'r') as f:
    clues = re.split("\d*?\.", f.read());
  print clues[0];
  print clues[1];

def changeClues(x):
  change = True;
  while(change == True):
    print x;
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

if __name__ == "__main__": 
  parse()
