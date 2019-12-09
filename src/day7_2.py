from util import iohandler, stringutil
from clazz import icc

import itertools

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
combinationDict = dict()


def calculate_signal(params):
    global intcodeArray

    amp_value = 0
    for par in params:
        ret_list = icc.IcComputer(intcodeArray, [par, amp_value]).calc_feedback_loop()
        amp_value = ret_list[0]
        intcodeArray = ret_list[1]

    return amp_value


permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
for perm in permutations:
    combinationDict.update({calculate_signal(perm): perm})

maxKey = 0
for key in combinationDict.keys():
    if key > maxKey:
        maxKey = key

# maxSignalPerm = stringutil.list_to_string(combinationDict.get(maxKey))

# --- solution ---

iohandler.end(str(maxKey))
