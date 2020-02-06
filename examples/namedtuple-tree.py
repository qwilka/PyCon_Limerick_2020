"""
"""
from collections import defaultdict, namedtuple

# def namedtuplenode():
#     return namedtuple("Node", ["name", "data", "children"], defaults=[{}, []])

namedtuplenode = lambda : namedtuple("Node", ["name", "data", "children"], defaults=[{}, []])

root = namedtuplenode()


