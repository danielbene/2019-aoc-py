from util import iohandler, stringutil
from clazz import icc

import itertools

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
combinationDict = dict()


# def calculate_signal(params):
#     global intcodeArray
#
#     amp_value = 0
#     amp_array = [0, 0, 0]
#     while 1:
#         for par in params:
#             # amp_value = icc.IcComputer(intcodeArray, [par, amp_value]).calculate()
#             amp_array = icc.IcComputer(intcodeArray, [par, amp_value]).calc_feedback_loop(amp_array[2])
#             amp_value = amp_array[0]
#             intcodeArray = amp_array[1]
#             print(par, amp_array[2], amp_array)

    # return amp_value


permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
for perm in permutations:
    # combinationDict.update({calculate_signal(perm): perm})
    amp_value = 0
    amp_array = [0, 0, 0, 0]
    for par in perm:
        # amp_value = icc.IcComputer(intcodeArray, [par, amp_value]).calculate()
        while amp_array[3] != 1:
            amp_array = icc.IcComputer(intcodeArray, [par, amp_value]).calc_feedback_loop(amp_array[2])
            amp_value = amp_array[0]
            intcodeArray = amp_array[1]
            print(par, amp_array[2], amp_array)

# maxKey = 0
# for key in combinationDict.keys():
#     if key > maxKey:
#         maxKey = key

# maxSignalPerm = stringutil.list_to_string(combinationDict.get(maxKey))

# print(str(maxKey))

# --- solution ---

iohandler.end(str(''))
