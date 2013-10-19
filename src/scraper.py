# scraper.py
from bs4 import BeautifulSoup
from clue import *
from board import *
import re
import urllib2
import numpy

#take in clue, length of answer

class Scraper(object):
	def run_scraper(self, clues, board):
		for c in clues:
                        if "DOWN" in c.clue_str:
                          continue
			if c.direction == Board.ACROSS:
				l = board[c.coord.x, c.coord.y].right_length
			if c.direction == Board.DOWN:
				l = board[c.coord.x, c.coord.y].down_length
			if l == None:
				print("Length is not being calculated correctly")
			self.get_answers(c, l)

	def get_answers(self, clue, length):
		"""get_answers(clue, length) will return a dictionary with key the clue 
		and value a list (without repetitions) of possible answers of length equal
		to length that is provided to the function"""
		original_clue = clue
		print(original_clue.clue_str)
		clue = self.check_clue(clue)
		stuff_to_check = []
		#get html from crosswordnexus.com
		try:
			if "%27" in clue:
				nexus_soup = self.url_to_soup("http://www.crosswordnexus.com/finder.php?clue="
					+ self.plus_clue(clue) + "&pattern=")
			else:
				nexus_soup = self.url_to_soup("http://www.crosswordnexus.com/finder.php?clue="
					+ self.hyphenate_clue(clue) + "&pattern=")
			big_a = nexus_soup.select("big a")
			stuff_to_check.append(big_a)
		except urllib2.HTTPError:
			print("Someting is wrong with getting the data from crosswordnexus.com")
		#get html from crosswordheaven.com
		try:
			heaven_soup = self.url_to_soup("http://www.crosswordheaven.com/search/result?clue="
				+ self.plus_clue(clue) + "&answer=")
			td_a = heaven_soup.select("td a")
			stuff_to_check.append(td_a)
		except urllib2.HTTPError:
			print("Something is wrong with getting the data from crosswordheaven.com")
		#get html from crosswordtracker.com
		try:
			tracker_soup = None
			if "%27" in clue or '"' in clue:
				tracker_soup = self.url_to_soup("http://www.crosswordtracker.com/search/?answer=&clue="
					+ self.plus_clue(clue))
			elif ' ' in clue:
				tracker_soup = self.url_to_soup("http://www.crosswordtracker.com/clue/" + self.hyphenate_clue(clue) + "/")
			else:
				print("Skipping this website for 1-word clue")
			if (tracker_soup):
				a = tracker_soup.select("a")
				stuff_to_check.append(a)
		except urllib2.HTTPError:
			print("Something is wrong with getting the data from crosswordtracker.com")
		#get words
		i = 0
		toReturn = []
		regex = re.compile("^[A-Z]+$")
		for stuff in stuff_to_check:
			i = 0;
			while (i < len(stuff)):
				data = stuff[i].contents[0]
				if ((len(data)==length) | (len(data)==(length-1))):
					if (regex.match(data)):
						if (data not in toReturn):
							if clue[-1] == 's':
								if (len(data)==length-1):
									toReturn.append(data+"S")
								else:
									toReturn.append(data)
							elif (len(data)==length):
								toReturn.append(data)
				i = i + 1
		original_clue.word_list = toReturn
		print(toReturn)

	def url_to_soup(self, url):
		""" Open site and soupify """
		opened = urllib2.urlopen(url)
		content = opened.read()
		soup = BeautifulSoup(content)
		return soup

	def hyphenate_clue(self, clue):
		return clue.replace(" ","-")

	def plus_clue(self, clue):
		return clue.replace(" ","+")

	def check_clue(self, clue):
		new_str = clue.clue_str
		if '(' in new_str:
			i = 0
			while (i < len(new_str)):
				if new_str[i]=='(':
					break
				i = i + 1
			new_str = new_str[0:i-1]
		if "'" in new_str:
			i = 0
			while (i < len(new_str)):
				if new_str[i]=="'":
					new_str = new_str[0:i] + "%27" + new_str[i+1:]
				i = i + 1
		return new_str
