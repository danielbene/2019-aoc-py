# simple util methods to simplify the redundant parts of the solutions
from datetime import datetime

inputFile = None
outputFile = None
startTime = None
endTime = None
# modify pattern to match your defaults
tsPattern = '%Y-%m-%d %H:%M:%S.%f'


def begin(puzzle):
    global inputFile, outputFile, startTime

    inputFile = open('../input/' + puzzle, 'r')
    outputFile = open('../solution/' + puzzle, 'w')
    startTime = datetime.strptime(str(datetime.now()), tsPattern).timestamp()

    return inputFile


def end(solution):
    global inputFile, outputFile, startTime, endTime

    endTime = datetime.strptime(str(datetime.now()), tsPattern).timestamp()
    outputFile.write('Solution: ' + str(solution) + '\n')
    outputFile.write('Runtime: ' + str(round(endTime - startTime, 3)) + ' sec\n')

    inputFile.close()
    outputFile.close()
