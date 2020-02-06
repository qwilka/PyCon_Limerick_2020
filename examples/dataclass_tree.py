from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class DataclassNode:
    name: str
    children: List[Any] = field(default_factory=lambda : [])
    data: Dict = field(default_factory=lambda : {})

    def add_child(self, childnode):
        self.children.append(childnode)
        return childnode
    
    def show(self, indent=2, _pre=""):
        print(_pre + self.name)
        for _c in self.children:
            _c.show(indent, _pre=_pre+" "*indent)
        


if __name__=="__main__":
    test1 = False
    test2 = False
    countries = True

    if test1:
        root = DataclassNode("root-node", data={"age":55})
        child1 = DataclassNode("child1", data={"age":28})
        root.children.append(child1)
        child2 = DataclassNode("child2")
        root.children.append(DataclassNode("child2"))
        child2.data["age"] = 25
        grandchild1 = DataclassNode("grandchild1")
        grandchild1.data["age"] = 1
        child1.children.append(grandchild1)
        root.show()

    if test2:
        root = DataclassNode("root-node", data={"age":77})
        child1 = root.add_child( DataclassNode("child 1", data={"age":54}) )
        child2 = root.add_child( DataclassNode("child 2") )
        child2.data["age"] = 52
        gchild1 =  child1.add_child( DataclassNode("grand-child 1") )
        gchild1.data["age"] = 23
        child1.add_child( DataclassNode("grand-child 2", data={"age":21})  )
        gchild1.add_child( DataclassNode("great-grand-child 1") )
        root.show()

    if countries:
        # https://www.worldometers.info/world-population/
        root = DataclassNode("World", data={"population":7762609412})
        europe = root.add_child( DataclassNode("Europe") )
        scandinavia = europe.add_child( DataclassNode("Scandinavia") )
        scandinavia.add_child( DataclassNode("Denmark", data={"population":5792202}) )
        scandinavia.add_child( DataclassNode("Sweden", data={"population":10099265}) )
        scandinavia.add_child( DataclassNode("Norway", data={"population":5421241}) )
        namerica = root.add_child( DataclassNode("North America") )
        namerica.add_child( DataclassNode("Canada", data={"population":37742154}) )
        root.show()
