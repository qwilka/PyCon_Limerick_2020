"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
import sys
from PyQt5.QtWidgets import ( QWidget, QVBoxLayout,
    QApplication, QTreeWidget, QTreeWidgetItem )

app = QApplication(sys.argv)
win = QWidget()
layout = QVBoxLayout(win)

tree = QTreeWidget()
tree.setHeaderLabels(['Name', 'capital city', "population"])

root = QTreeWidgetItem(tree, ['The World'])
europe = QTreeWidgetItem(root, ['Europe'])
QTreeWidgetItem(europe, ['Belgium', "Brussels", "11515793"])
QTreeWidgetItem(europe, ['Greece', "Athens", "10768477"])
scandinavia = QTreeWidgetItem(europe, ['Scandinavia'])
QTreeWidgetItem(europe, ['Spain', "Madrid", "46733038"])
denmark = QTreeWidgetItem(scandinavia, ['Denmark', "Copenhagen", "5822763"])
QTreeWidgetItem(scandinavia, ['Sweden', "Stockholm", "10302984"])
QTreeWidgetItem(scandinavia, ['Norway', "Oslo", "5421241"])
QTreeWidgetItem(scandinavia, ['Iceland', "Reykjavík", "364260"])
QTreeWidgetItem(scandinavia, ['Finland', "Helsinki", "5521158"])
QTreeWidgetItem(denmark, [ "Faroe Islands"])
QTreeWidgetItem(denmark, [ "Greenland"])
samerica = QTreeWidgetItem(root, ['South America'])
QTreeWidgetItem(samerica, ['Chile', "Santiago", "17574003"])
 
layout.addWidget(tree)
win.show()
sys.exit(app.exec_())
