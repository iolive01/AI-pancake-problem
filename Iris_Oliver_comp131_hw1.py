############################################################################### 
# Comp 131 Assignment 1
# Iris Oliver
# Collaborated with Leah Stern, Cathy Cowell, Ki Ki Chan

###############################################################################
# INSTRUCTIONS FOR USE
# 
#	To run the program: python Iris_Oliver_comp131_hw1.py 
#	To modify the input, change the "initial" value on line 102. To make 
#	finding this value easy, you can search in this text file for the
#	keyword MODIFYME
#
#
###############################################################################
# Problem 1: Define the problem as a searching problem
#
#	To define this problem as a searching problem, we will consider the 5 
#	characteristics of a search problem and how they apply to the pancake
#	problem.
#
#	1. Initial State
#		We consider the initial state of the problem to be the starting 
#		configuration of pancakes, eg [3,4,5,1,2], or [4,5,2,1,3]
#
#	2. Goal State
#		The Goal State is all of the pancakes stacked with the largest on 
#		the bottom and the smallest on the top; the array would be [1,2,3,4,5].
#	
#	3. Path Cost Function
#		Each path has an equal weight, since each flip costs an equal amount
#		to perform. Let all the weights be 1, for simplicity. 
#
#	4. Successor Function
#		To proceed with the search, we flip the stack of pancakes. Each flip
#		is the expansion of the frontier.
#
#	5. Possibilities
#		The possibilities are all the permumations of the 5 pancakes. At each 
#		node there are 3 possibilities available, representing the 3 different
#		points at which the cook can insert the spatula to flip the pancakes 
#		(technically, there are 4 possible places to insert the spatula, but 
#		since flipping only the top-most pancakes is trivial, we omit this 
#		case). 
#

###############################################################################
# Problem 2: Define a possible cost function (backward cost)

# The backward cost is the same as the number of flips. We can calculate
# this by observing the length of the path array which we accumulate.
def backwardCost(path):
	return len(path)


###############################################################################
# Problem 3: Define a possible heuristic function (forward cost)

# We will use the gap method as outlined in the paper as our heuristic function.
def findGaps(pancakeStack):
	list(pancakeStack)
	gaps = 0
	for i in range(len(pancakeStack) - 1):
		if (abs(pancakeStack[i] - pancakeStack[i + 1]) != 1):
			gaps += 1
	return gaps


###############################################################################
# Problem 4: Implement an A* algorithm in your language of preference

# Flips the stack at the given flip position
# Arguments: the index to flip at, a number between 1-4, and a tuple, the 
#			stack of pancakes
# Returns: a tuple, the flipped stack
def flipStack(flipPos, pancakeStack):
	pancakeList = list(pancakeStack)
	notFlippedSide = pancakeList[0:flipPos]
	flippedSide = pancakeList[flipPos:]
	flippedSide.reverse()
	flippedStack = notFlippedSide + flippedSide
	return tuple(flippedStack)

# Prints the path in a legible format.
def printPath(path):
	currVal = ()
	nodesPrinted = 0
	while nodesPrinted < len(path):
		for child, parent in path.items():
			if parent == currVal:
				print child, "-->",
				currVal = child
				nodesPrinted += 1


# Reads input from the user, and starts the search. Initializes the data
# structures used in the search algorithm.
def startSearch():
	frontier = {}
	path = {}
	visited = []

	# MODIFYME Input a new initial state here! MODIFYME 
	# for example: initial = tuple([3,4,2,1,5])
	initial = tuple([1,5,3,4,2])
	goal = tuple([1,2,3,4,5])
	aStar(initial, goal, frontier, path, visited)

# Implements the A* search algorithm
# Arguments: the initial state (tuple), the goal state (tuple), a dictionary 
#			 representing the frontier, and a dictionary representing the 
#			 current path
# Returns: none
def aStar(initial, goal, frontier, path, visited):
	
	# initialize all the data structures
	frontier[initial] = 0
	path[initial] = ()
	visited.append(initial)

	while (frontier):

		# find the minimum cost value - algorithm from 
		# https://www.w3resource.com/python-exercises/dictionary/
		#				python-data-type-dictionary-exercise-15.php
		current = min(frontier.keys(), key=(lambda k: frontier[k]))
		
		# pop the minimum value
		frontier.pop(current) 	

		if current == goal:
			print "Initial State: ", initial
			print "Goal State: ", goal
			print "Path: ", printPath(path)
			print "Number of Flips (cost): ", (len(path) - 1)
			print "Number of Nodes Visited: ", len(visited)
			break

		for i in range(1, len(current) - 1):
			flipped = flipStack(i, current)
			if flipped not in visited:
				curCost = findGaps(flipped) + (len(path) - 1)
				frontier[flipped] = curCost

		# keep track of the current node in the path
		minNewChild = min(frontier.keys(), key=(lambda k: frontier[k]))
		path[minNewChild] = current
		visited.append(current)

startSearch()











