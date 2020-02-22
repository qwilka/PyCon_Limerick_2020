"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
import sys
from PyQt5.QtWidgets import QApplication, QTreeView  
from nodes import vntree_from_vndict
from models import VnTreeModel


dict_ = {
    "name": "The World",
    "_childs" : [
        {
            "name": "Europe",
            "_childs": [
                {"name": "Belgium"},
                {"name": "Greece"},
                {
                    "name": "Scandinavia",
                    "_childs": [
                        {
                            "name": "Denmark",
                            "_childs": [
                                {"name": "Faroe Islands"},
                                {"name": "Greenland"},
                            ]
                        },
                        {"name": "Sweden"},
                        {"name": "Norway"},
                        {"name": "Iceland"},
                        {"name": "Finland"},
                    ]
                },
                {"name": "Spain"},
            ]
        },
        {
            "name": "South America",
            "_childs": [
                {"name": "Chile"}
            ]
        },                
    ]
}
rootnode = vntree_from_vndict(dict_)
model = VnTreeModel(rootnode)
app = QApplication(sys.argv)
treeView = QTreeView()
treeView.show()
treeView.setModel(model)
sys.exit(app.exec_())