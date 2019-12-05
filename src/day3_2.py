from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

redWire = inputFile.readline().split(',')
blueWire = inputFile.readline().split(',')

redWireCoords = []
redWireSteps = []
blueWireCoords = []
blueWireSteps = []


def calculate_steps(input, output, steps_array):
    global redWireCoords, blueWireCoords, redWireSteps, blueWireSteps
    current_position = [0, 0]
    step_counter = 0

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
            step_counter += 1
            coord = [current_position[0] + mod[0], current_position[1] + mod[1]]
            steps_array.append(step_counter)
            output.append(tuple(coord))
            current_position = coord


calculate_steps(redWire, redWireCoords, redWireSteps)
calculate_steps(blueWire, blueWireCoords, blueWireSteps)

intersections = list(set(redWireCoords).intersection(blueWireCoords))
intersectionSteps = []

for intersection in intersections:
    intersectionSteps.append([redWireSteps[int(redWireCoords.index(intersection))] +
                              blueWireSteps[int(blueWireCoords.index(intersection))]])

# --- solution ---

iohandler.end(str(min(intersectionSteps))[1:-1])
