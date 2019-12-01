from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

fuel = 0
additionalFuel = 0  # using global var to handle the lack of reference passing


def mass_requirement(mass):
    return int(float(mass) / 3) - 2  # conversion handles the floor rounding


def mass_recursion(module_fuel):
    global additionalFuel

    addition = mass_requirement(module_fuel)
    if addition > 0:
        additionalFuel += addition
        mass_recursion(addition)


def with_additional_mass(module_mass):
    module_fuel = mass_requirement(module_mass)
    mass_recursion(module_fuel)
    return module_fuel + additionalFuel


for module in inputFile:
    additionalFuel = 0
    fuel += with_additional_mass(module)

# --- solution ---

iohandler.end(str(fuel))
