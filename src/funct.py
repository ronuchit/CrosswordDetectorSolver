
#where x is list of words.
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
