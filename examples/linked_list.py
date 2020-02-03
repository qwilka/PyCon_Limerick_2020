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
        return newnode 
    
    def __iter__(self):
        yield self
        for node in itertools.chain(iter(self.next)):
            yield node

    def __reversed__(self):
        for node in itertools.chain(reversed(self.next)):
            yield node
        yield self

    def to_text(self, indent=2):
        for ii, _n in enumerate(self):
            if ii==0:
                stg = "|-- " + _n.name
            else:
                stg += "\n" + "  "*indent*ii + "+-> "  + _n.name
        print(stg)


if __name__ == '__main__':
    if False:
        first  = Node('First Node')
        second = Node('Second Node', first)
        third = Node('Third Node', second)
        third.append(Node('Fourth Node'))
        for n in first:
            print(n.name)
        for n in reversed(first):
            print(n.name)
    if True:
        # http://www.gutenberg.org/files/4217/4217-h/4217-h.htm
        root = Node('Stephen Dedalus')
        (root.append(Node('Class of Elements'))
        .append(Node('Clongowes Wood College'))
        .append(Node('Sallins'))
        .append(Node('County Kildare')) 
        .append(Node('Ireland'))
        .append(Node('Europe'))
        .append(Node('The World'))
        .append(Node('The Universe'))
        )
        root.to_text()