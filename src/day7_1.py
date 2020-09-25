from itertools import permutations
from util import iohandler, stringutil
from clazz import icc

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
combinationDict = dict()


def calculate_signal(params):
    amp_value = 0
    for par in params:
        amp_value = icc.IcComputer(intcodeArray, [par, amp_value]).calculate()

    return amp_value


permutations = list(permutations([0, 1, 2, 3, 4]))
for perm in permutations:
    combinationDict.update({calculate_signal(perm): perm})

maxKey = 0
for key in combinationDict.keys():
    if key > maxKey:
        maxKey = key

# maxSignalPerm = stringutil.list_to_string(combinationDict.get(maxKey))

# --- solution ---

iohandler.end(str(maxKey))
