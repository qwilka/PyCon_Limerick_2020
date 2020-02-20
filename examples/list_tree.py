
def quicktree(depth, nchildren=2):
    t = [n for n in range(nchildren)] 
    for d in range(depth):
        t = [ t for n in range(nchildren)]
    return t


if __name__ == "__main__":
    import pprint
    # quick quadtree
    qt = quicktree(depth=2, nchildren=4)
    pprint.pprint(qt, indent=2, width=20)

