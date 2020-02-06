"""
One-line Tree in Python
https://gist.github.com/hrldcpr/2012250  

Also relevant:
https://news.ycombinator.com/item?id=3881171
https://stackoverflow.com/questions/651794/whats-the-best-way-to-initialize-a-dict-of-dicts-in-python/651879#651879
"""
from collections import defaultdict
import json


def onelinetree(): return defaultdict(onelinetree)


if __name__=="__main__":
    root = onelinetree()
    root["The World"]
    root["The World"]["population"] = 7762609412
    root["The World"]["Europe"]
    root["The World"]["Europe"]["Scandinavia"]
    root["The World"]["Europe"]["Scandinavia"]["Denmark"]
    root["The World"]["Europe"]["Scandinavia"]["Denmark"]["population"] = 5792202
    root["The World"]["Europe"]["Scandinavia"]["Sweden"]
    root["The World"]["Europe"]["Scandinavia"]["Sweden"]["population"] = 10099265
    root["The World"]["Europe"]["Scandinavia"]["Norway"]
    root["The World"]["Europe"]["Scandinavia"]["Norway"]["population"] = 5421241
    root["The World"]["North America"]
    root["The World"]["North America"]["Canada"]
    root["The World"]["North America"]["Canada"]["population"] = 37742154
    print(json.dumps(root, indent=2))


