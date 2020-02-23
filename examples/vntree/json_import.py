"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
from vntree import Node

jsonfilepath = "countries.json"

theworld = {
    "name": "The World",
    "childs" : [
        {
            "name": "Europe",
            "childs": [
                {
                    "name": "Belgium",
                    "data": {
                        "capital": "Brussels",
                        "population": 11515793
                    }
                },
                {
                    "name": "Greece",
                    "data": {
                        "capital": "Athens",
                        "population": 10768477
                    }
                },
                {
                    "name": "Scandinavia",
                    "childs": [
                        {
                            "name": "Denmark",
                            "data": {
                                "capital": "Copenhagen",
                                "population": 5822763
                            },
                            "childs": [
                                {"name": "Faroe Islands"},
                                {"name": "Greenland"},
                            ]
                        },
                        {
                            "name": "Sweden",
                            "data": {
                                "capital": "Stockholm",
                                "population": 10302984
                            }
                        },
                        {
                            "name": "Norway",
                            "data": {
                                "capital": "Oslo",
                                "population": 5421241
                            }
                        },
                        {
                            "name": "Iceland",
                            "data": {
                                "capital": "Reykjavík",
                                "population": 364260
                            }
                        },
                        {
                            "name": "Finland",
                            "data": {
                                "capital": "Helsinki",
                                "population": 5521158
                            }
                        },
                    ]
                },
                {
                    "name": "Spain",
                    "data": {
                        "capital": "Madrid",
                        "population": 46733038
                    }
                },
            ]
        },
        {
            "name": "South America",
            "childs": [
                {
                    "name": "Chile",
                    "data": {
                        "capital": "Santiago",
                        "population": 17574003
                    }
                }
            ]
        },                
    ]
}

dicttree = Node(treedict=theworld)
print("Countries tree from dictionary (dicttree):")
dicttree.show()

# save dicttree in a JSON file
dicttree.to_json(jsonfilepath)

# Round-trip, create a new tree from the JSON file
print(f"Countries tree from JSON file {jsonfilepath}:")
jsontree = Node.from_json(jsonfilepath)
jsontree.show()

# Compare trees dicttree and jsontree
# diff is a comparison indicator in range 0-1.0
# 1.0 is a perfect match
comp = dicttree.tree_compare(jsontree)
print(f"jsontree round-trip comparison with dicttree = {comp}")