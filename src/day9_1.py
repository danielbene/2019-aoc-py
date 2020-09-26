from util import iohandler
from clazz import icc

inputFile = iohandler.begin(__file__)

# --- solution ---

intcodeArray = list(map(int, inputFile.readline().split(',')))
combinationDict = dict()


print(icc.IcComputer(intcodeArray, []).calculate())

# --- solution ---

iohandler.end(str('solution'))
