# simple util methods to simplify the redundant parts of the solutions
import os
from util import dateutil

inputFile = None
outputFile = None
startTime = None
endTime = None


def begin(script_path):
    global inputFile, outputFile, startTime

    puzzle = os.path.basename(os.path.normpath(script_path)[:-3])
    inputFile = open('../input/' + puzzle, 'r')
    outputFile = open('../solution/' + puzzle, 'w')
    startTime = dateutil.current_formatted_timestamp()

    return inputFile


def end(solution):
    global inputFile, outputFile, startTime, endTime

    endTime = dateutil.current_formatted_timestamp()
    outputFile.write('Solution: ' + str(solution) + '\n')
    outputFile.write('Runtime: ' + str(round(endTime - startTime, 3)) + ' sec\n')

    inputFile.close()
    outputFile.close()
