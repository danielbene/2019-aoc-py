from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

fuel = 0

for module in inputFile:
    fuel += int(float(module) / 3) - 2  # conversion handles the floor rounding

# --- solution ---

iohandler.end(str(fuel))
