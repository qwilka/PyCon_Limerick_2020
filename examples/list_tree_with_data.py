"""
Copyright © 2020 Stephen McEntee
Licensed under the MIT license. 
https://github.com/qwilka/PyCon_Limerick_2020/blob/master/examples/LICENSE
"""
import json
from pprint import pprint

root = ["The World", {"population":7762609412}]
europe = ["Europe", {"population":737000000}]
root.append(europe)
scandinavia = ["Scandinavia", {"population":31000000}]
europe.append(scandinavia)
scandinavia.append( ["Denmark", {"population":5792202}] )
scandinavia.append( ["Sweden", {"population":10099265}] )
#scandinavia.append( ["Norway", {"population":5421241}] )
namerica = ["North America", {"population":367914615}]
root.append(namerica)
namerica.append( ["Canada", {"population":37742154}] ) 

pprint(root, indent=4, compact=True)

