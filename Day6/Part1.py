from pathlib import Path

def solve(filePath:Path) -> int:
	''' Finds the number of overlapping sections for elf cleaning assignments.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Integer representing the answer.
	'''
	with open(filePath, 'r', encoding='UTF-8') as dataFile:
		data = dataFile.readline()
		for it in range(len(data) - 5):
			if isUnique(data[it:it+4]):
				return it + 4


def isUnique(checkStr:str) -> bool:
	'''Checks the list or string to see if they are unique.

	Arguments:
		checkStr(str): String in question to check if the string is unique.
	'''
	for char in checkStr:
		if checkStr.count(char) > 1:
			return False

	return True
