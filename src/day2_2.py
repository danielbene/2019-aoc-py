from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))


def calc(pos_a: int, pos_b: int):
    tmp_array = intcodeArray.copy()
    position = 0
    tmp_array[1] = pos_a
    tmp_array[2] = pos_b

    while position <= len(tmp_array):
        if tmp_array[position] == 99:
            break
        else:
            if tmp_array[position] == 1:
                tmp_array[tmp_array[position + 3]] = \
                    tmp_array[tmp_array[position + 1]] + tmp_array[tmp_array[position + 2]]
            else:
                tmp_array[tmp_array[position + 3]] = \
                    tmp_array[tmp_array[position + 1]] * tmp_array[tmp_array[position + 2]]
        position += 4

    return tmp_array[0]


baseValue = 19690720 - calc(12, 2)
nounInc = (calc(2, 0) - calc(1, 0))
verbInc = (calc(0, 2) - calc(0, 1))

if nounInc > verbInc:
    noun = 12 + int(float(baseValue / nounInc))
    verb = 2 + int(float(baseValue % nounInc / verbInc))
else:
    verb = 2 + int(float(baseValue / verbInc))
    noun = 12 + int(float(baseValue % verbInc / nounInc))

output = 100 * noun + verb

# --- solution ---

iohandler.end(str(output))
