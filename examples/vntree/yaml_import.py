"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
from vntree import Node

yamlfilepath = "countries.yaml"

rootnode = Node.yaml2tree(yamlfilepath)
rootnode.show()

iceland = rootnode.find_one_node("name", value="Iceland")
if iceland:
    capital = iceland.get_data("capital")
    pop = iceland.get_data("population")
    print(f"The capital city of {iceland.name} is {capital}\nThe population of {iceland.name} is {pop}")
