from pathlib import Path
from typing import List

def solve(file_path:Path) -> int:
	''' Gives you the sum of all your points for the given RPS file.
	Arguments:
		file_path(pathlib.Path): The filepath in which to read elf data from.

	Returns:
		Integer representing number of points if following the guide that is input_file
	'''
	return sum(get_RPS_scores(file_path))

def get_RPS_scores(file_path:Path) -> List[int]:
	''' Reads rock-paper-scissors plays from a file and returns the total "points"

	Naming:
		A, X: rock
		B, Y: paper
		C, Z: scissors

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
		file_path(pathlib.Path): The filepath in which to read elf data from.

	Returns:
		List of integer representing number of points if following the guide that is input_file
	'''

	# Reading in our file and splitting on newlines
	round_data = []
	with open(file_path, 'r', encoding='UTF-8') as input_file:
		round_data = input_file.readlines()

	# Lets iterate through each of our rounds finding the results
	score_data = []
	for round in round_data:
		score_data.append(score_RPS(round))

	return score_data

def score_RPS(round_data) -> int:
	''' Takes in a single game of rock paper scissors and returns the score.

	Naming:
		A, X: rock
		B, Y: paper
		C, Z: scissors

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
	''' Making both answers the same value + 1

	Alright, listen up

	ord is a python function that turns alphabetical characters into ordinals.
	chr reverses that

	i.e. ord('X') is 88, ord('A') is 65
	Here is a table for continence https://www.johndcook.com/ascii.png

	Now lets talk about scoring. If we ordinate our answer and minus 87, we just get our score. i.e. ord('X') - 87 == 1.

	Now lets talk about solving. To start (stay with me), we'll ordinate our vote, remove 23, then characterize. This results in our votes being in the same field as our opponents. i.e. rock = A, paper = B...
	Dual is simple, if we match, we draw
	To check for winning, we can simply check if ours is one higher or two lower
		a - b (+1)
		b - c (+1)
		or
		c - a (-2)
	else this and we have our no win.
	'''
	score = 0
	# Splitting and iterating our values
	data = [ord(value) for value in round_data.strip().split(' ')]

	# Alright, lets move our choice to the same as our opponents
	data[1] = data[1] - 23

	# Counting our score
	score += data[1] - 64

	# Checking for draw
	if data[0] == data[1]:
		return score + 3

	# Checking for win
	if data[1] in [data[0] + 1, data[0] - 2]:
		return score + 6

	# If we got here, we've lost, lets just return our score
	return score