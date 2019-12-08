from util import iohandler, treeutil
from anytree import Node, Walker, WalkError

inputFile = iohandler.begin(__file__)

# --- solution ---

planetTree = []
orbitPairs = dict()
directOrbitNum = 0
indirectOrbitNum = 0

# building the base dictionary
for orbit in inputFile:
    orbit_pair = orbit.split(')')
    if orbitPairs.get(orbit_pair[0]) is None:
        orbitPairs.update({orbit_pair[0]: [orbit_pair[1][:3]]})
    else:
        orbitPairs.get(orbit_pair[0]).append(orbit_pair[1][:3])

planetTree.append(Node('COM'))
currentParent = 'COM'

com = planetTree[0]
you_parent = None
san_parent = None


def build_tree(parent, childs):
    global indirectOrbitNum, directOrbitNum, you_parent, san_parent
    for planet_names in childs:
        planet_node = Node(planet_names, parent=parent)
        planetTree.append(planet_node)

        if planet_names == 'YOU':
            you_parent = planet_node.parent
        elif planet_names == 'SAN':
            san_parent = planet_node.parent

        indirectOrbitNum += len(planet_node.ancestors) - 1
        directOrbitNum += 1

        if orbitPairs.get(planet_names) is not None:
            build_tree(planet_node, orbitPairs.pop(planet_names))


build_tree(com, orbitPairs.pop(currentParent))

w = Walker()

# first node is not a step -> remove
# if it's stupid, but it works...
steps = ''.join(list(str(w.walk(you_parent, san_parent)).split(',')[1:])).count('Node')

# --- solution ---

iohandler.end(str(steps))
