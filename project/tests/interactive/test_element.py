from models.tree import ElementNode, tree_to_string, generate_tree
from models.xml_parser import XMLTree

def basic_node_test():
    root = ElementNode('root', 'folder', True, '')
    src = ElementNode('src', 'folder', True, '', root)
    util = ElementNode('util', 'folder', True, root)
    read_me = ElementNode('README', 'file', True, '.rst', root)
    util = ElementNode('util', 'folder', True, '', root)
    print(tree_to_string(root))


def element_parse_test():
    xml = XMLTree('/Users/michael/prog/python/python3/project_creator/design'
                  '/examples/hierarchy_config.xml')
    tree = generate_tree(xml)
    print(tree.__str__())
