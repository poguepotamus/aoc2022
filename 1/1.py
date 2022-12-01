#!/usr/env python310

import sys
from pathlib import Path

# Getting our input file path
inFileName = Path() / '1' / 'example.txt' if len(sys.argv) != 2 else sys.argv[1]

with open(inFileName, 'r', encoding='UTF-8') as inFile:
	elfCals = [sum([int(cal) for cal in elf.split('\n')]) for elf in inFile.read().strip().split('\n\n')]
	print(max(elfCals))