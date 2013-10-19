#!/usr/bin/env python 
import clue
import re

def parse():
  with open('clues.txt', 'r') as f:
    clues = re.split("\d*?\.", f.read());
  print clues[0];
  print clues[1];

if __name__ == "__main__": 
  parse()

