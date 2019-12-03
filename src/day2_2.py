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

# this is a bit cheesy, but the rocket researches show that position 1 value increases output value by 256k,
# and position 2 value increases that by 1
noun = intcodeArray[1] + int(float((19690720 - intcodeArray[0]) / 256000))
verb = intcodeArray[2] + int(float((19690720 - intcodeArray[0]) % 256000))
output = 100 * noun + verb

# --- solution ---

iohandler.end(str(output))
