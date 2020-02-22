"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
import sys
try:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.simpledialog import askstring
except Exception as err:
    print(" ERROR: unable to find required Python module «tkinter» \n", err)
    sys.exit(1)


class TreeApp(Frame):
    def __init__(self, parent, dicttree=None):
        self.parent = parent
        self.frame = Frame.__init__(self, parent)
        self.treeview = Treeview(self.frame)
        self.treeview.pack(side='left', fill='both', expand=True)
        vsbar = Scrollbar(self.frame, orient="vertical",command=self.treeview.yview)
        vsbar.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=vsbar.set)
        self.pack(fill='both', expand=True)
        #vsbar['command'] = self.treeview.yview
        #self.treeview['yscrollcommand'] = vsbar.set
        #vsbar.pack(side=RIGHT, fill=Y, before=self.treeview)
        

        # self.treeview.grid(column=0, row=0, sticky='nsew')
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.parent.grid_columnconfigure(0, weight=1)
        # self.parent.grid_rowconfigure(0, weight=1)


        if dicttree and isinstance(dicttree, dict):
            self.load_dicttree(dicttree)
        else:
            _root = self.treeview.insert("", "end", text="root-node")
            _c1 = self.treeview.insert(_root, "end", text="child 1")
            _c2 = self.treeview.insert(_root, "end", text="child 2")
            self.treeview.insert(_c2, "end", text="granchild 1")
                
        self.treeview.bind("<Double-1>", self.onDoubleClick)
        

    def onDoubleClick(self, event):
        item = self.treeview.selection()[0]
        print("Node clicked:", self.treeview.item(item,"text"))
    
    def load_dicttree(self, dicttree, parent=""):
        if "name" in dicttree:
            _id = self.treeview.insert(parent, "end", text=dicttree["name"])
        if "_childs" in dicttree and isinstance(dicttree["_childs"], list):
            for _n in dicttree["_childs"]:
                self.load_dicttree( _n, parent=_id)
        return True




if __name__ == "__main__":
    theworld = {
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
    approot = Tk()
    approot.title("ttk Treeview")
    app = TreeApp(approot, dicttree=theworld)
    #app = TreeApp(approot)
    approot.mainloop()

