from pathlib import Path
from typing import List

def solve(file_path:Path) -> float:
	''' Reads elf information from file and parses the calorie count that's highest for a single elf.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read elf data from.

	Returns:
		A single integer representing the highest calorie count for a single elf.
	'''
	# First, we'll get our file information
	file_data = ''
	with open(file_path, 'r', encoding='UTF-8') as in_file:
		file_data = in_file.read().strip()

	# Now, lets parse that data into a list and cast our strings to ints
	elf_data = _parse_elf_data(file_data)

	# Now we just need to find the max calories for our elf
	return max(elf_data)


def _parse_elf_data(elf_data_string:str) -> List[int]:
	''' Parses elf data from a string.

	Typically this string comes from a file.
	Each calorie count is separated by a newline and each elf is separated by two newlines.

	Arguments:
		elf_data_string(str): The string data from a file that contains calorie counts for each elf

	Returns:
		A list containing the total calorie count for each elf.
	'''
	# Lets split our calories up unto a list per elf
	elf_data = elf_data_string.split('\n\n')

	# Then, lets split each elf's data up by newlines and parse
	for i, elf in enumerate(elf_data):
		calories = elf.split('\n')
		# And while we're here, lets cast these values to an int
		calories = [int(value) for value in calories]
		# We want the result to be the sum, we can do that
		elf_data[i] = sum(calories)

	# Now we have a 2D list containing integers for calories
	return elf_data