import xml.etree.ElementTree as eTree
maxdepth = 0


def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = eTree.ElementTree(eTree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
