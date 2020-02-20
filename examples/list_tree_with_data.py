import json
from pprint import pprint

root = ["The World", {"population":7762609412}]
europe = ["Europe", {"population":737000000}]
root.append(europe)
scandinavia = ["Scandinavia", {"population":31000000}]
europe.append(scandinavia)
scandinavia.append( ["Denmark", {"population":5792202}] )
scandinavia.append( ["Sweden", {"population":10099265}] )
scandinavia.append( ["Norway", {"population":5421241}] )
namerica = ["North America", {"population":367914615}]
root.append(namerica)
namerica.append( ["Canada", {"population":37742154}] ) 

pprint(root, indent=4, compact=True)

if False:
    root = ["world"]
    europe = ["Europe"]
    root.append(europe)
    scandinavia = ["Scandinavia"]
    europe.append(scandinavia)
    scandinavia.append( ["Denmark"] )
    scandinavia.append( ["Sweden"] )
    scandinavia.append( ["Norway"] )
    namerica = ["North America"]
    root.append(namerica)
    namerica.append( ["Canada"] ) 

    print(json.dumps(root, indent=4))
