from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

# two wires, one per input lines
# find the closest intersection to the central port
# directions: R,L,U,D, and the number represent the distance/steps in that direction
# we need the CLOSEST intersection TO THE CENTRAL if multiple are present
# distance is the sum of the x,y axis so like 3+3=6
# they start from the SAME POINT somewhere in the grid

grid = [[], []]
redWire = inputFile.readline().split(',')
blueWire = inputFile.readline().split(',')



print(redWire)
print(blueWire)
# --- solution ---

iohandler.end(str(''))
