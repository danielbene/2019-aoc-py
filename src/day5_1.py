from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

# 1 - three param - addition
# 2 - three param - multiplication

# two new opcode instruction 3 and 4
# 3 single param -> takes an int from input (stdin?) and saves to the position defined by the param
# 4 single param -> outputs the value to the address by the param

# parameter modes
# 0 -> as before param shows the position to get the value from
# 1 immediate mode -> param represent value so 50 is 50
# eg: 11002 -> ABCDE (A mode of 3rd param, B mode of 2nd param, C mode of 1st param, DE opcode)


# parameters that an istruction writes to will never be in immediate mode?!!!
# instruction pointer should be incremented according to opcode param num
# ints can be negative

# input should be stdin (always 1 input), probably part 2 will use it differently
# output shows the state of the test, not 0 means thers an error
#   - final output is the answer (if every other is 0)

intcodeArray = list(map(int, inputFile.readline().split(',')))
position = 0
usrInput = 0


def get_param_modes(value):
    value += 10000
    return [get_int_pos(value, 0)-1, get_int_pos(value, 1), get_int_pos(value, 2)]


def get_int_pos(int_value, pos):
    return int(str(int_value)[pos])


def zero_mode(position_num) -> int:
    return int(intcodeArray[intcodeArray[position_num]])


def first_mode(position_num) -> int:
    return int(intcodeArray[position_num])


def calculate(param_mode_array, opcode):
    if param_mode_array[2] == 0:
        second = zero_mode(position + 1)
    else:
        second = first_mode(position + 1)

    if param_mode_array[1] == 0:
        third = zero_mode(position + 2)
    else:
        third = first_mode(position + 2)

    if opcode == 1:
        if param_mode_array[0] == 0:
            intcodeArray[first_mode(position + 3)] = second + third
        else:
            intcodeArray[position + 3] = second + third
    elif opcode == 2:
        if param_mode_array[0] == 0:
            intcodeArray[first_mode(position + 3)] = second * third
        else:
            intcodeArray[position + 3] = second * third
    else:
        print('----------------FAIL1----------------')


while position <= len(intcodeArray):
    value = intcodeArray[position]
    if value == 99:
        print('BREAK')
        break

    opcode = get_int_pos(value, -1)
    param_modes = get_param_modes(value)

    print(value, opcode, param_modes)
    print(intcodeArray)

    if opcode == 1 or opcode == 2:
        calculate(param_modes, opcode)
    elif opcode == 3:
        intcodeArray[first_mode(position + 1)] = int(input('Give me input, ya\' filthy bastard: '))
    elif opcode == 4:
        print('#######MODE_4#######', intcodeArray[position + 1])
    else:
        print('----------------FAIL2----------------', opcode)

    print(intcodeArray)

    if opcode == 1 or opcode == 2:
        position += 4
    else:
        position += 2

# --- solution ---

iohandler.end(str(''))
