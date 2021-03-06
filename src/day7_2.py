from itertools import permutations
from util import iohandler
from clazz import icc

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
combinationDict = dict()


def calculate_signal(params):
    first = True
    amp_value = 0
    amps = [icc.IcComputer(intcodeArray, [par, amp_value]) for par in params]
    while True:
        for amp in amps:
            if amp_value != icc.IcComputer.exit_value:
                amp_value = amp.feedback(amp_value, first)
            elif len(amps)-1 != 0 and amp != amps[len(amps)-1]:
                amps.remove(amp)  # removing exited amplifiers
            else:
                return amp.zero_mode(amp.diagCode)

        first = False


permutations = list(permutations([5, 6, 7, 8, 9]))
for perm in permutations:
    combinationDict.update({calculate_signal(perm): perm})

maxKey = 0
for key in combinationDict.keys():
    if key > maxKey:
        maxKey = key

# --- solution ---

iohandler.end(str(maxKey))
