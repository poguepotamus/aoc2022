from pathlib import Path
from typing import List

def solve(file_path:Path) -> int:
	''' Finds the sum of priorities in a given file.

	Arguments:
		file_path(pathlib.Path): The filepath in which to read data from.

	Returns:
		Integer representing the answer.
	'''
	with open(file_path, 'r', encoding='UTF-8') as data_file:
		data = data_file.readlines()

	# Parsing our rucksack data to return the duplicate item
	data = [find_duplicate_item(rucksack) for rucksack in data]

	# Iterating through our letters to find the actual priority
	data = [find_priority(duplicate_item) for duplicate_item in data]

	return sum(data)


def find_priority(item:str) -> int:
	''' Finds the priority for the given item.

	Arguments:
		item(str): The item represented as a single character

	Returns:
		Integer representing the items priority
	'''
	if item.isupper():
		return ord(item) - 38

	return ord(item) - 96


def find_duplicate_item(rucksack_data:str) -> str:
	''' Takes in the string representing the rucksack data and returns the item that exists in both it's compartments.

	Arguments:
		rucksack_data(str): The items that are in the rucksack represented by a string of alphabetical characters.

	Returns:
		A single character that is duplicated in the front half and back half of the string.
	'''
	# Simple first task, lets split the data in half
	half_len = int(len(rucksack_data) / 2)
	top_compartment = rucksack_data[:half_len]
	bottom_compartment = rucksack_data[half_len:]

	# Then we find the first duplicate letter
	for letter in top_compartment:
		if letter in bottom_compartment:
			return letter

	return None