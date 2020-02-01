import itertools

class Node:
    """Node class for linked list data structure.  
    Ref: https://en.wikipedia.org/wiki/Tree_(data_structure)
    """
    def __init__(self, name, previous=None, data=None):
        self.name = name
        if previous and isinstance(previous, Node):
            previous.append(self)
        else:
            self.previous = None
        self.next = ()   # iterable null value required to satisfy __iter__ protocol
        self.data = data

    def append(self, newnode):
        self.next = newnode
        newnode.previous = self
        return True 

    def __iter__(self):
        yield self
        for node in itertools.chain(iter(self.next)):
            yield node

    def __reversed__(self):
        for node in itertools.chain(reversed(self.next)):
            yield node
        yield self


if __name__ == '__main__':
    first  = Node('First Node')
    second = Node('Second Node', first)
    third = Node('Third Node', second)
    third.append(Node('Fourth Node'))
    for n in first:
        print(n.name)
    for n in reversed(first):
        print(n.name)