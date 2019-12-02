from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
position = 0

intcodeArray[1] = 12
intcodeArray[2] = 2

while position <= len(intcodeArray):
    if intcodeArray[position] == 99:
        break
    else:
        if intcodeArray[position] == 1:
            intcodeArray[intcodeArray[position + 3]] = \
                intcodeArray[intcodeArray[position + 1]] + intcodeArray[intcodeArray[position + 2]]
        else:
            intcodeArray[intcodeArray[position + 3]] = \
                intcodeArray[intcodeArray[position + 1]] * intcodeArray[intcodeArray[position + 2]]
    position += 4

# --- solution ---

iohandler.end(str(intcodeArray[0]))
