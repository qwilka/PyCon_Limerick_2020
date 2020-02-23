"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""

description = """Print a basic example of a list-based tree."""


def quicktree(depth, nchildren=2):
    """Make a fully developed tree based on nested lists.
    """
    t = [n for n in range(nchildren)] 
    for d in range(depth):
        t = [ t for n in range(nchildren)]
    return t


if __name__ == "__main__":
    import argparse
    import pprint

    aparser = argparse.ArgumentParser(description=description)
    aparser.add_argument("case", help="Specify an example case to run.", 
        nargs='?', default="list",
        choices=["list", "binary", "quad"])
    args = aparser.parse_args()

    if args.case == "list":
        # $ python list_tree_simple.py list 
        # a list is an "internal" (folder or group) node
        # non-list nodes are "leaf" (terminal) nodes
        rootnode = list()
        europe = list(); rootnode.append(europe)
        europe.append("Belgium")
        europe.append("Greece")
        scandinavia = list(); europe.append(scandinavia)
        denmark = list(); scandinavia.append(denmark)
        scandinavia.extend(["Norway", "Sweden", "Iceland", "Finland"])
        denmark.extend(["Faroe Islands", "Greenland"])
        europe.append("Spain")
        samerica = list(); rootnode.append(samerica)
        samerica.append("Chile")
        pprint.pprint(rootnode, indent=2, width=40)


    if args.case == "quad":
        # $ python list_tree_simple.py quad
        # quick quadtree
        qt = quicktree(depth=2, nchildren=4)
        pprint.pprint(qt, indent=2, width=20)

    if args.case == "binary":
        # $ python list_tree_simple.py binary
        # quick binary tree
        bt = quicktree(depth=3, nchildren=2)
        pprint.pprint(bt, indent=2, width=20)
