from pathlib import Path

from Day4 import Part1

def solve(file_path:Path) -> int:
	''' Finds the number of overlapping sections for elf cleaning assignments.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Integer representing the answer.
	'''
	cleaning_assignments = Part1.read_data(file_path)

	return (sum([cleaning_overlaps(assignment) for assignment in cleaning_assignments]))

def cleaning_overlaps(cleaning_assignment) -> bool:
	''' Determines if one cleaning assignment overlaps

	Arguments:
		cleaning_assignment(tuple(tuple(int))): A tuple of tuples containing integers for each cleaning assignment.

	Returns:
		Returns a boolean if one cleaning assignment overlaps the other
	'''
	first_elf = cleaning_assignment[0]
	second_elf = cleaning_assignment[1]

	if first_elf[0] <= second_elf[0] <= first_elf[1]:
		return True
	if first_elf[0] <= second_elf[1] <= first_elf[1]:
		return True
	if second_elf[0] <= first_elf[0] <= second_elf[1]:
		return True
	if second_elf[0] <= first_elf[1] <= second_elf[1]:
		return True

	return False