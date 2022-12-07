from pathlib import Path

from Day6 import Part1

def solve(filePath:Path) -> int:
	''' Finds the number of overlapping sections for elf cleaning assignments.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Integer representing the answer.
	'''
	with open(filePath, 'r', encoding='UTF-8') as dataFile:
		data = dataFile.readline()
		for it in range(len(data) - 15):
			if Part1.isUnique(data[it:it+14]):
				return it + 14
