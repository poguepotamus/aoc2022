from pathlib import Path

class SupplyStacks:
	''' Represents stacks of supplies identified by characters.

	Optional Arguments:
		filePath(pathlib.Path): The file in which to read supply stack information.
		stackData(str): The string that contains the stack information.
	'''
	def __init__(self, filePath:Path=None, stackData:str=None):
		self.stacks = []

		# If we have a string, we'll load from that first.
		if stackData:
			self.loadFromString(stackData)

		elif filePath:
			self.loadFromFile(filePath.resolve())


	def __str__(self):
		# Iterating through our stacks to print our information
		# Just like how we're loading, we're going to write this backwards and print it out
		listHeaders = '   '.join([str(it+1) for it in range(len(self.stacks))])
		output = [f' {listHeaders} ']

		# Finding tallest stack
		tallestStack = max([len(stack) for stack in self.stacks])

		# We know how tall the message needs to be, so we create each of those rows
		for row in range(tallestStack):
			rowOut = ''
			# For each row, we iterate through the stacks
			for stack in self.stacks:
				# Writing either the data for the cargo or a blank line
				if row < len(stack):
					rowOut += f'[{stack[row]}] '
				else:
					rowOut += '    '

			# Moving to the next row
			output.append(f'{rowOut}\n')

		# Now that all our data is in our list, we reverse the list
		output.reverse()
		# And return it
		return ''.join(output)


	def loadFromFile(self, filePath:Path):
		''' Reads in stack information from a file.

		Expects a double line in between the stack information and the rest of the file.

		Arguments:
			filePath(pathlib.Path): The path to the file to read our data from.
		'''
		with open(filePath, 'r', encoding='UTF-8') as dataFile:
			self.loadFromString(dataFile.read().split('\n\n')[0])


	def loadFromString(self, stackData:str):
		''' Reads in stack information from a string.

		Arguments:
			stackData(str): The string that contains the stack information.
		'''
		# Most important information is how many stacks we have, so lets split and reverse our lines.
		stackDataLists = [_ for _ in stackData.split('\n') if _ != '']
		maxLen = max([len(_) for _ in stackDataLists])
		stackDataLists = [_.ljust(maxLen, ' ') for _ in stackDataLists]
		stackDataLists.reverse()

		# Now that we have our list count first, lets grab the number of lists we're working with
		numStacks = len(stackDataLists[0][1::4])

		# Creating our blank 2D array to hold our supply information
		self.stacks = [[] for _ in range(numStacks)]
		# for _ in range(0, numStacks+1):
		# 	self.stacks.append([])

		# Now we iterate through the rest of our data
		for row in stackDataLists[1:]:
			# Iterating through each of our stacks
			for stackNum, cargoName in enumerate(row[1::4]):
				# If our cargo isn't empty, append our cargo to the stack
				if cargoName != ' ':
					self.stacks[stackNum].append(cargoName)


	def move(self, sourceStack:int, resultStack:int, index:int=1):
		''' Moves a piece of cargo from one stack to the other.

		Arguments:
			sourceStack(int): The stack in which to pull the cargo from.
			resultStack(int): The stack in which to place our cargo.
			index(int): How the stack system was ordinated. i.e. was it a 0-index or 1-index system.
				Default: 1
		'''
		cargo = self.stacks[sourceStack - index].pop()
		self.stacks[resultStack - index].append(cargo)

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
		for _ in range(count):
			supplyStacks.move(source, result, index=1)

	# Printing our supplyStacks to get our result
	print(supplyStacks)

	# Returning a string of the top of all our stacks
	return ''.join([stack[-1] for stack in supplyStacks.stacks])


if __name__ == '__main__':

	print('Executing main function')
	supplyStacks = SupplyStacks(Path() / 'Day5' / 'example.txt')
	print(supplyStacks)
	pass
