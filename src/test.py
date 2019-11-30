# solution from 2018 aoc day1_1 for environment testing
from util import IOhandler

inputFile = IOhandler.begin('test')

# --- solution ---

frequency = 0

for line in inputFile:
    if line[0] == '+':
        frequency += int(line[1:])
    else:
        frequency -= int(line[1:])

# --- solution ---

IOhandler.end(frequency)
