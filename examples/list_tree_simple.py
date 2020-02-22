"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""

def quicktree(depth, nchildren=2):
    """Make a fully developed tree based on nested lists.
    """
    t = [n for n in range(nchildren)] 
    for d in range(depth):
        t = [ t for n in range(nchildren)]
    return t


if __name__ == "__main__":
    import pprint

    LIST_TREE = True
    BINARYTREE_QUICK = False
    QUADTREE_QUICK = False

    if LIST_TREE:
        # a list is an "internal" (folder or group) node
        # non-list nodes are "leaf" (terminal) nodes
        rootnode = list()
        child1 = list(); rootnode.append(child1)
        child1.append("grandchild1 (leaf node)")
        child1.append("grandchild2 (another leaf)")
        child2 = list(); rootnode.append(child2)
        grandchild3 = "grandchild3"; child1.append(grandchild3)
        grandchild4 = list(); child1.append(grandchild4)
        grandchild4.extend([1, "two", [], {"data":1234}])
        child3 = "child3"; rootnode.append(child3)
        pprint.pprint(rootnode, indent=2, width=40)


    if QUADTREE_QUICK:
        # quick quadtree
        qt = quicktree(depth=2, nchildren=4)
        pprint.pprint(qt, indent=2, width=20)

    if BINARYTREE_QUICK:
        # quick binary tree
        bt = quicktree(depth=3, nchildren=2)
        pprint.pprint(bt, indent=2, width=20)
