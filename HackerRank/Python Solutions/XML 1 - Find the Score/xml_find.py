import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    count = 0
    for tag in node:
        count = count + get_attr_number(tag)
    return count + len(node.attrib)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
