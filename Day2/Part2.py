from pathlib import Path

from Day1.Part1 import _parse_elf_data

def solve(file_path:Path) -> int:
	''' Gives you the solution for the appropriate advent of code question.
	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Answer for the appropriate advent of code questions.
	'''
	round_data = []
	with open(file_path, 'r', encoding='UTF-8') as input_file:
		round_data = input_file.readlines()

	# Iterating through our rounds and finding the results
	score_data = []
	for round in round_data:
		score_data.append(score_RPS(round))

	return sum(score_data)

def score_RPS(round_data) -> int:
	''' Takes in a single game of rock paper scissors and returns the score.

	This is for the second part of day2_2022, the second column is for what the result of the round should be.

	Naming:
		A: rock
		B: paper
		C: scissors

		X: lose
		Y: draw
		Z: win

	Scoring:
		By Choice:
			Rock: 1
			Paper: 2
			Scissors: 3
		By outcome:
			Win: 6
			Draw: 3
			Loss: 0

	Arguments:
		String representing two choices, your opponents and yours, split by a space.

	Returns:
		Integer representing number of point you would get for that round.
	'''
	''' See Day1 for ord and chr explanations.

	We'll use the second column to make a key for calculating our choice score.
	key = x:0 y:1 z:2, so second column - 87

	Lets draw a table for points by choice, then think about our scores being 0 indexed, then mod 3 by adding 3 to everything
	  A | B | C       A | B | C       A | B | C
	X 3 | 1 | 2     x 2 | 0 | 1     x 2 | 3 | 4
	Y 1 | 2 | 3     y 0 | 1 | 2     y 3 | 4 | 5
	Z 2 | 3 | 1     z 1 | 2 | 0     z 4 | 5 | 6

	So if we ordinate our first column (A-63=2), add the key from our second column, then mod 3, we have a 0 indexed score. Add 1 and we get our score.

	Then using the key, can just multiply by 3 to get our win score.
	x:loss:0
	y:draw:3
	z:win:6
	'''
	data = [ord(value) for value in round_data.strip().split(' ')]

	# Creating our key with the second column and ord our first column
	data[1] = data[1] - 88
	data[0] = data[0] - 64

	# Capturing our score
	choice_score = ((data[0] + 1 + data[1]) % 3) + 1

	# Now finding our status score
	status_score = (data[1] * 3)

	return status_score + choice_score