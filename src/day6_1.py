from util import iohandler, treeutil
from anytree import Node

inputFile = iohandler.begin(__file__)

# --- solution ---

# https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python-are-there-any-built-in-data-structures-in

planetTree = []
orbitPairs = dict()
directOrbitNum = 0
indirectOrbitNum = 0

for orbit in inputFile:
    orbit_pair = orbit.split(')')
    if orbitPairs.get(orbit_pair[0]) is None:
        orbitPairs.update({orbit_pair[0]: [orbit_pair[1][:3]]})
    else:
        orbitPairs.get(orbit_pair[0]).append(orbit_pair[1][:3])

planetTree.append(Node('COM'))
currentParent = 'COM'
com = planetTree[0]


def build_tree(parent, childs):
    global indirectOrbitNum, directOrbitNum
    for planet_names in childs:
        planet_node = Node(planet_names, parent=parent)
        planetTree.append(planet_node)

        indirectOrbitNum += len(planet_node.ancestors) - 1
        directOrbitNum += 1

        if orbitPairs.get(planet_names) is not None:
            build_tree(planet_node, orbitPairs.pop(planet_names))


build_tree(com, orbitPairs.pop(currentParent))
print(orbitPairs)
print(directOrbitNum, indirectOrbitNum)
# treeutil.save_tree_layout(com, 'day6_1_treemap')

# --- solution ---

iohandler.end(str(''))
