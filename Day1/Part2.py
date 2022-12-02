from pathlib import Path

from Day1.Part1 import _parse_elf_data

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

	# Now we just need to find the top three elfs by calories held
	elf_data.sort()
	return sum(elf_data[-3:])




