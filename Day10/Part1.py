from pathlib import Path
from re import split as re_split

from Day10 import SignalStrengthCalculator as SSC

def solve(filePath:Path) -> int:
	''' Finds the number of overlapping sections for elf cleaning assignments.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Integer representing the answer.
	'''
	with open(filePath, 'r', encoding='UTF-8') as dataFile:
		fileData = re_split('\n| ', dataFile.read())
		return SSC.calcSignalStrength(fileData)
