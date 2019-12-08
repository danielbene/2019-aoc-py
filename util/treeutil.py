from util import iohandler
from anytree import RenderTree


# this is for visualising the planet connections as ascii map
def save_tree_layout(com, filename):
    treefile = iohandler.open_local('solution', filename, 'w')
    for pre, fill, node in RenderTree(com):
        treefile.write("%s%s\n" % (pre, node.name))

    treefile.close()
