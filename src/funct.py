
#where x is list of words.
def changeClues(x):
		change = True;
		while(change == True):
			print x;
			answer = rawinput("Do you want to change anything?")
			if(answer == "yes"):
				index = rawinput("Which number do you want to change?")
				x[int(index)] = rawinput("Change to:?")
			else:
				print "no"
				change = False
		return x
