_commands = ['addx', 'noop']

def calcSignalStrength(data:list[str]) -> int:
	''' Calculates the signal strength given a list of data.

	Arguments:
		data(list[str]): A list of strings, which is the data input file separated by any whitespace characters.
	'''
	signalStrengths = {}
	register = 1

	for num, command in enumerate(data):
		# Getting our cycle Number
		cycle = num + 1

		# Checking our cycle number and adding the current signal strength
		if (cycle) % 40 == 20:
			signalStrengths[cycle] = cycle * register

		# Adding value to our register
		if command not in _commands:
			register += int(command)

	return sum(signalStrengths.values())

def writeCRT(data:list[str]) -> str:
	''' Finds the image on the CRT

	Arguments:
		data(list[str]): A list of strings, which is the data input file separated by any whitespace characters.
	'''
	screen = ['']
	register = 1

	for num, command in enumerate(data):
		# Getting our cycle Number
		cycle = num + 1

		crtPos = len(screen[-1])
		if abs(crtPos - register) <= 1:
			screen[-1] += '#'
		else:
			screen[-1] += '.'

		# Checking our cycle number and adding the current signal strength
		if (cycle) % 40 == 0:
			screen.append('')

		# Adding value to our register
		if command not in _commands:
			register += int(command)

	return '\n'.join(screen)