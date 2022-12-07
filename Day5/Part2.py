from pathlib import Path

from Day5 import Part1


class SupplyStacks(Part1.SupplyStacks):
	def moveMany(self, sourceStack:int, resultStack:int, count:int=1, index:int=1):
		''' Moves a piece of cargo from one stack to the other.

		Arguments:
			sourceStack(int): The stack in which to pull the cargo from.
			resultStack(int): The stack in which to place our cargo.
			count(int): Number of items to move to the new stack.
			index(int): How the stack system was ordinated. i.e. was it a 0-index or 1-index system.
				Default: 1
		'''
		cargo = self.stacks[sourceStack - index][-count:]
		del self.stacks[sourceStack - index][-count:]
		self.stacks[resultStack - index] += cargo

def solve(filePath:Path) -> str:
	''' Finds the sum of priorities in a given file.

	Arguments:
		filePath(pathlib.Path): The filepath in which to read data from.

	Returns:
		A string with the name of all the supply stack tops
	'''
	# Opening our filepath and splitting our cargo stacks from our commands
	with open(filePath, 'r', encoding='UTF-8') as dataFile:
		cargoData, commands = dataFile.read().split('\n\n')

	# Now, lets create our supply stacks
	supplyStacks = SupplyStacks(stackData=cargoData)

	# Iterating through our commands and feeding them to the supply stack
	for command in commands.splitlines():
		count, source, result = [int(_) for _ in command.split(' ')[1::2]]
		supplyStacks.moveMany(source, result, count=count, index=1)

	# Printing our supplyStacks to get our result
	print(supplyStacks)

	# Returning a string of the top of all our stacks
	return ''.join([stack[-1] for stack in supplyStacks.stacks])
