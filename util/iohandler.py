# simple util methods to simplify the redundant parts of the solutions
import os
from util import dateutil

inputFile = None
outputFile = None
startTime = None


def begin(script_path):
    global inputFile, outputFile, startTime

    puzzle = os.path.basename(os.path.normpath(script_path)[:-3])
    inputFile = open_local('input', puzzle[:-2], 'r')
    outputFile = open_local('solution', puzzle, 'w')

    startTime = dateutil.current_timestamp()

    return inputFile


def end(solution: str):
    global inputFile, outputFile, startTime

    # python's naming conventions are weird
    end_time = dateutil.current_timestamp()

    outputFile.write('{:<12}{}'.format('Solution:', solution) + '\n')
    outputFile.write('{:<12}{}'.format('Runtime:', str(round(end_time - startTime, 4))) + ' sec\n')

    inputFile.close()
    outputFile.close()


def open_local(folder: str, file: str, mode: str):
    separator = os.path.sep
    return open(os.getcwd() + separator + folder + separator + file, mode, encoding='utf-8')
