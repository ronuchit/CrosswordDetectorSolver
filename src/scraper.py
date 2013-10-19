# scraper.py
from bs4 import BeautifulSoup
import re
import urllib2
#import numpy

#take in clue, length of answer

def get_answers(clue, length):
	"""get_answers(clue, length) will return a dictionary with key the clue 
	and value a list (without repetitions) of possible answers of length equal
	to length that is provided to the function"""
	original_clue = clue
	clue = check_clue(clue);
	#get html from crosswordnexus.com
	stuff_to_check = []
	nexus_soup = url_to_soup("http://www.crosswordnexus.com/finder.php?clue="
		+ hyphenate_clue(clue) + "&pattern=")
	big_a = nexus_soup.select("big a")
	stuff_to_check.append(big_a)
	#get html from crosswordheaven.com
	heaven_soup = url_to_soup("http://www.crosswordheaven.com/search/result?clue="
		+ plus_clue(clue) + "&answer=")
	td_a = heaven_soup.select("td a")
	stuff_to_check.append(td_a)
	#get html from crosswordtracker.com
	tracker_soup = None
	if ' ' in clue:
		tracker_soup = url_to_soup("http://www.crosswordtracker.com/clue/" + hyphenate_clue(clue) + "/")
	else:
		print("Skipping this website for 1-word clue")
	if (tracker_soup):
		a = tracker_soup.select("a")
		stuff_to_check.append(a)
	#get words
	i = 0
	toReturn = []
	regex = re.compile("^[A-Z]+$")
	for stuff in stuff_to_check:
		i = 0;
		while (i < len(stuff)):
			data = stuff[i].contents[0]
			if (len(data)==length):
				if (regex.match(data)):
					if (data not in toReturn):
						toReturn.append(data)
			i = i + 1
	toReturn = {original_clue: toReturn}
	return toReturn

def url_to_soup(url):
	""" Open site and soupify """
	opened = urllib2.urlopen(url)
	content = opened.read()
	soup = BeautifulSoup(content)
	return soup

def hyphenate_clue(clue):
	return clue.replace(" ","-")

def plus_clue(clue):
	return clue.replace(" ","+")

def check_clue(clue):
	if '(' in clue:
		i = 0;
		while (i < len(clue)):
			if clue[i]=='(':
				break
			i = i + 1
		clue = clue[0:i-1]
	return clue

#print(get_answers("death",4))
#print(get_answers("sense of self", 3))
