import itertools
import os
import sys


class Node:
    """Node class for tree data structure.  
    Ref: https://en.wikipedia.org/wiki/Tree_(data_structure)
    """
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        if parent and isinstance(parent, Node):
            parent.add_child(self)
        elif parent is None:
            self.parent = None
            self._show_traversal = False  # print messages in __iter__ and __reversed__ methods
        else:
            raise TypeError("Node instance «{}» argument «parent» type not valid: {}".format(name, type(parent)))
        

    def __str__(self):
        _level = len(self.get_ancestors())
        return "{} «{}» level={} coord={}".format(self.__class__.__name__, self.name, _level, self._coord)


    """
    https://docs.python.org/3/library/itertools.html
    https://realpython.com/python-itertools/
    https://pymotw.com/3/itertools/index.html
    https://realpython.com/introduction-to-python-generators/
    """
    def __iter__(self): 
        if self._root._show_traversal: print(f":self: «{self.name}»")
        yield self  
        for ii, node in enumerate(itertools.chain(*map(iter, self.children))):
            if self._root._show_traversal: print(f":{ii}: «{node.name}» «{self.name}»")
            yield node 


    def __reversed__(self):  
        for ii, node in enumerate(itertools.chain(*map(reversed, reversed(self.children)))):
            if self._root._show_traversal: print(f":{ii}: «{node.name}» «{self.name}»")
            yield node
        if self._root._show_traversal: print(f":self: «{self.name}»")
        yield self 


    def add_child(self, newnode):
        self.children.append(newnode)
        newnode.parent = self
        return newnode    


    def get_ancestors(self):
        ancestors=[]
        _curnode = self
        while _curnode.parent:
            _curnode = _curnode.parent
            ancestors.append(_curnode)
        return ancestors


    @property
    def _root(self):
        _n = self
        while _n.parent:
            _n = _n.parent
        return _n


    @property
    def _coord(self):
        _coord = []
        _node = self
        while _node.parent:
            _idx = _node.parent.children.index(_node)
            _coord.insert(0, _idx)
            _node = _node.parent
        return tuple(_coord)


    def to_texttree(self):
        treetext = ""
        root_level = len(self.get_ancestors())
        for node in self: 
            level = len(node.get_ancestors()) - root_level
            treetext += ("." + " "*3)*level + "|---{}\n".format(node.name)
        return treetext



if __name__ == '__main__':

    SIMPLE_TREE = True
    TOP_DOWN_TRAVERSAL = False
    BOTTOM_UP_TRAVERSAL = False

    if SIMPLE_TREE:
        rootnode = Node('root-node')
        child = Node('child', rootnode)
        gchild = child.add_child( Node('grand-child') )
        gchild.add_child( Node('great-grand-child') )
        print(rootnode.to_texttree())
        rootnode._show_traversal = True
        print("\nTree traverse top-down:")
        for node in rootnode:
            print(node)    
        print("\nTree traverse bottom-up:")
        for node in reversed(rootnode):
            print(node)


    if TOP_DOWN_TRAVERSAL or BOTTOM_UP_TRAVERSAL:
        rootnode   = Node('ROOT ("top" of the tree)')
        Node("1st child (leaf node)", parent=rootnode)
        child2 = Node("2nd child", rootnode)
        Node("grand-child1 (leaf node)", child2)
        Node("grand-child2 (leaf node)", child2)
        child3 = Node("3rd child", rootnode)
        Node("another child (leaf node)", rootnode)
        grandchild3 = Node(parent=child3, name="grand-child3")
        ggrandchild = Node("great-grandchild", grandchild3)
        Node("great-great-grandchild (leaf node)", ggrandchild)
        Node("great-grandchild2 (leaf node)", grandchild3)
        print()
        print(rootnode.to_texttree())

    if TOP_DOWN_TRAVERSAL:
        # switch-on tracing messages in __iter__ method:
        rootnode._show_traversal = True
        print("\nTree iterate top-down:")
        for node in rootnode:
            print(node)

    if BOTTOM_UP_TRAVERSAL:
        # switch-on tracing messages in __reversed__ method:
        rootnode._show_traversal = True
        print("\nTree iterate bottom-up:")
        for node in reversed(rootnode):
            print(node)

