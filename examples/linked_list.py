"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
import itertools

class LLnode:
    """Class for linked list data structure.  
    Ref: https://en.wikipedia.org/wiki/Linked_list
    """
    def __init__(self, value, prev=None):
        # self.prev = prev
        # if prev: prev.append(self)
        if prev and isinstance(prev, LLnode):
            prev.append(self)
        else:
            self.prev = None
        self.next = ()   # iterable null value required to satisfy __iter__ protocol
        self.value = value

    def append(self, newnode):
        self.next = newnode
        newnode.prev = self
        return newnode 
    
    def __iter__(self):
        yield self
        for node in itertools.chain(iter(self.next)):
            yield node

    def __reversed__(self):
        for node in itertools.chain(reversed(self.next)):
            yield node
        yield self

    def show(self, display=True, indent=2):
        for ii, node in enumerate(self):
            if ii==0:
                stg = "|-- " + node.value
            else:
                stg += "\n" + "  "*indent*ii + "+-> "  + node.value
        if display:
            print(stg)
        else:
            return stg


if __name__ == '__main__':
    if True:
        first  = LLnode('First Node')
        second = LLnode('Second Node', first)
        third = LLnode('Third Node', second)
        third.append(LLnode('Fourth Node'))
        for n in first:
            print(n.value)
        for n in reversed(first):
            print(n.value)
    if True:
        # http://www.gutenberg.org/files/4217/4217-h/4217-h.htm
        root = LLnode('Stephen Dedalus')
        (root.append(LLnode('Class of Elements'))
        .append(LLnode('Clongowes Wood College'))
        .append(LLnode('Sallins'))
        .append(LLnode('County Kildare')) 
        .append(LLnode('Ireland'))
        .append(LLnode('Europe'))
        .append(LLnode('The World'))
        .append(LLnode('The Universe'))
        )
        root.show()