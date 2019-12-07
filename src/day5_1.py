from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
position = 0
usrInput = 0
diagCode = 0


def get_param_modes(value):
    value += 10000
    return [get_int_pos(value, 0)-1, get_int_pos(value, 1), get_int_pos(value, 2)]


def get_int_pos(int_value, pos):
    return int(str(int_value)[pos])


def zero_mode(position_num) -> int:
    return int(intcodeArray[intcodeArray[position_num]])


def first_mode(position_num) -> int:
    return int(intcodeArray[position_num])


def get_param_value_by_mode(param_mode_array):
    first = zero_mode(position + 1) if param_mode_array[2] == 0 else first_mode(position + 1)
    second = zero_mode(position + 2) if param_mode_array[1] == 0 else first_mode(position + 2)
    # this is different, because we need only the position num to the array element assignment
    third = first_mode(position + 3) if param_mode_array[0] == 0 else position + 3

    return [first, second, third]


def calculate(opcode_value, opcode):
    params = get_param_value_by_mode(get_param_modes(opcode_value))
    intcodeArray[params[2]] = params[0] + params[1] if opcode == 1 else params[0] * params[1]


while position <= len(intcodeArray):
    opcode_value = intcodeArray[position]
    if opcode_value == 99:
        break

    opcode = get_int_pos(opcode_value, -1)

    if opcode == 1 or opcode == 2:
        calculate(opcode_value, opcode)
        position += 4
    elif opcode == 3:
        intcodeArray[first_mode(position + 1)] = 1  # int(input('Give me input, ya\' filthy bastard: '))
        position += 2
    elif opcode == 4:
        diagCode = position + 1
        position += 2

# --- solution ---

iohandler.end(str(zero_mode(diagCode)))
