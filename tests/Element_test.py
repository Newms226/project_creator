from models.element_node import ElementNode, tree_to_string
import xml.etree.ElementTree as ET

def basic_node_test():
    root = ElementNode('root', 'folder', True, '')
    src = ElementNode('src', 'folder', True, '', root)
    util = ElementNode('util', 'folder', True, root)
    read_me = ElementNode('README', 'file', True, '.rst', root)
    util = ElementNode('util', 'folder', True, '', root)
    print(tree_to_string(root))

def element_parse_test()
