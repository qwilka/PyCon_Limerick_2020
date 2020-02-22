"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
from tkinter import *
from tkinter.ttk import *

app = Tk()
app.title("ttk_treeview_basic.py")

tree = Treeview(app)
tree["columns"]=("capital", "pop")
tree.column("capital", width=100, anchor="w" )
tree.column("pop", width=100)
tree.heading("capital", text="capital city")
tree.heading("pop", text="population")

root = tree.insert("", 0, text="The World")
europe = tree.insert(root, "end", text="Europe")
tree.insert(europe, "end", text="Belgium", values=("Brussels", 11515793))
tree.insert(europe, "end", text="Greece", values=("Athens", 10768477))
scandinavia = tree.insert(europe, "end", text="Scandinavia")
tree.insert(europe, "end", text="Spain", values=("Madrid", 46733038))
denmark = tree.insert(scandinavia, "end", text="Denmark", values=("Copenhagen", 5822763))
tree.insert(scandinavia, "end", text="Sweden", values=("Stockholm", 10302984))
tree.insert(scandinavia, "end", text="Norway", values=("Oslo", 5421241))
tree.insert(scandinavia, "end", text="Iceland", values=("Reykjavík", 364260))
tree.insert(scandinavia, "end", text="Finland", values=("Helsinki", 5521158))
tree.insert(denmark, "end", text="Faroe Islands")
tree.insert(denmark, "end", text="Greenland")
samerica = tree.insert(root, "end", text="South America")
tree.insert(samerica, "end", text="Chile", values=("Santiago", 17574003))

tree.pack(fill=BOTH, expand=True)

app.mainloop()
