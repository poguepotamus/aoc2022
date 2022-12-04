from pathlib import Path
from typing import List

def solve(file_path:Path) -> int:
	''' Finds the number of overlapping sections for elf cleaning assignments.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Integer representing the answer.
	'''
	cleaning_assignments = read_data(file_path)

	return(sum([cleaning_contains(assignment) for assignment in cleaning_assignments]))


def read_data(data_file_path:Path) -> List:
	''' Reads in the data for the specific problem and returns the most valuable data type

	Day 4 has us reading in two elves range of cleaning zones. I think the best way to order them is a list of tuples of tuples containing integers.

	Arguments:
		data_file_path(pathlib.Path): A path to the datafile to read in.

	Returns:
		Returns a list representing the data file in the most useful way possible.
	'''
	output = []
	with open(data_file_path, 'r', encoding='UTF-8') as data_file:
		for line in data_file.readlines():
			elves = line.split(',')
			elves = [tuple([int(section) for section in elf.split('-')]) for elf in elves]
			output.append(tuple(elves))

	return output


def cleaning_contains(cleaning_assignment) -> bool:
	''' Determines if one cleaning assignment contains the other.

	Arguments:
		cleaning_assignment(tuple(tuple(int))): A tuple of tuples containing integers for each cleaning assignment.

	Returns:
		Returns a boolean if one cleaning assignment fully contains the other.
	'''
	first_elf = cleaning_assignment[0]
	second_elf = cleaning_assignment[1]

	# If our first elf contains our second elf
	if first_elf[0] <= second_elf[0]:
		if first_elf[1] >= second_elf[1]:
			return True

	# If our second elf contains our first elf
	if second_elf[0] <= first_elf[0]:
		if second_elf[1] >= first_elf[1]:
			return True

	# If we haven't returned at this point, we don't have an assignment that contains another, we can return false.
	return False