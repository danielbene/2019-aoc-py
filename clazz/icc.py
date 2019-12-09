def get_param_modes(value):
    value += 10000
    return [get_int_pos(value, 0) - 1, get_int_pos(value, 1), get_int_pos(value, 2)]


def get_int_pos(int_value, pos):
    return int(str(int_value)[pos])


class IcComputer:
    intcodeArray = []
    usrInput = list()
    position = 0
    diagCode = 0

    def __init__(self, ic_array, usrInput):
        self.intcodeArray = ic_array
        self.position = 0
        self.diagCode = 0
        self.usrInput.append(usrInput[1])
        self.usrInput.append(usrInput[0])

    def zero_mode(self, position_num) -> int:
        return int(self.intcodeArray[self.intcodeArray[position_num]])

    def first_mode(self, position_num) -> int:
        return int(self.intcodeArray[position_num])

    def get_param_value_by_mode(self, param_mode_array):
        first = self.zero_mode(self.position + 1) if param_mode_array[2] == 0 else self.first_mode(self.position + 1)
        second = self.zero_mode(self.position + 2) if param_mode_array[1] == 0 else self.first_mode(self.position + 2)
        # this is different, because we need only the position num to the array element assignment
        third = self.first_mode(self.position + 3) if param_mode_array[0] == 0 else self.position + 3

        return [first, second, third]

    # handles opcode 1 and 2
    def calculate_values(self, opcode_value, opcode):
        params = self.get_param_value_by_mode(get_param_modes(opcode_value))
        self.intcodeArray[params[2]] = params[0] + params[1] if opcode == 1 else params[0] * params[1]

    # handles opcode 5 and 6
    def calculate_jumps(self, opcode_value, opcode):
        params = self.get_param_value_by_mode(get_param_modes(opcode_value))
        if opcode == 5:
            self.position = params[1] if params[0] != 0 else self.position + 3
        else:
            self.position = params[1] if params[0] == 0 else self.position + 3

    # handles opcode 7 and 8
    def calculate_equality(self, opcode_value, opcode):
        params = self.get_param_value_by_mode(get_param_modes(opcode_value))
        if opcode == 7:
            self.intcodeArray[params[2]] = 1 if params[0] < params[1] else 0
        else:
            self.intcodeArray[params[2]] = 1 if params[0] == params[1] else 0

    def calculate(self):
        while self.position <= len(self.intcodeArray):
            opcode_value = self.intcodeArray[self.position]
            if opcode_value == 99:
                break

            opcode = get_int_pos(opcode_value, -1)

            if opcode == 1 or opcode == 2:
                self.calculate_values(opcode_value, opcode)
                self.position += 4
            elif opcode == 3:
                self.intcodeArray[self.first_mode(self.position + 1)] =\
                    self.usrInput.pop(len(self.usrInput) - 1)
                self.position += 2
            elif opcode == 4:
                self.diagCode = self.position + 1
                self.position += 2
            elif opcode == 5 or opcode == 6:
                self.calculate_jumps(opcode_value, opcode)
            elif opcode == 7 or opcode == 8:
                self.calculate_equality(opcode_value, opcode)
                self.position += 4

        return self.zero_mode(self.diagCode)

    def calc_feedback_loop(self):
        return [self.calculate(), self.intcodeArray]
