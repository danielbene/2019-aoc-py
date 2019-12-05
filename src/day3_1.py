from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

redWire = inputFile.readline().split(',')
blueWire = inputFile.readline().split(',')

redWireCoords = []
blueWireCoords = []


def calculate_path(input, output):
    global redWireCoords, blueWireCoords
    current_position = [0, 0]

    for step in input:
        if step[0] == 'R':
            mod = [1, 0]
        elif step[0] == 'L':
            mod = [-1, 0]
        elif step[0] == 'U':
            mod = [0, 1]
        else:
            mod = [0, -1]

        for i in range(int(step[1:])):
            coord = [current_position[0] + mod[0], current_position[1] + mod[1]]
            output.append(tuple(coord))
            current_position = coord


calculate_path(redWire, redWireCoords)
calculate_path(blueWire, blueWireCoords)

intersections = list(set(redWireCoords).intersection(blueWireCoords))
manhattans = []

for intersection in intersections:
    intersection = list(intersection)

    if intersection[0] < 0:
        intersection[0] *= -1

    if intersection[1] < 0:
        intersection[1] *= -1

    manhattans.append(intersection[0] + intersection[1])

# --- solution ---

iohandler.end(str(min(manhattans)))
