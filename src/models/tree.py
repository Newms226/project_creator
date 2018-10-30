from anytree import RenderTree, NodeMixin

from models import FOLDER_STR, FILE_STR, IMPORT_STR, NodeBase, XMLElement
from models.xml_parser import Unit, get_name, get_element_type, get_git_status, \
    get_element_suffix, XMLTree


def tree_to_string(root: NodeMixin) -> str:
    _str = ''

    for pre, _, node in RenderTree(root):
        _str += f'{pre}{node}\n'

    return _str


class Tree(object):

    def __init__(self, root_node: NodeMixin): self.root = root_node

    def get_root(self) -> NodeMixin: return self.root

    def get_rendered_tree(self): return RenderTree(self.root)

    def __str__(self): return tree_to_string(self.root)


class ElementNode(NodeBase):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, element: XMLElement, parent: NodeBase = None):
        self.unit = Unit(name=name,
                         element_type=element_type,
                         git_track=git_track,
                         suffix=suffix)
        self.parent = parent
        self.xml_element = element

    def __str__(self):
        return self.unit.__str__()

    def __full_str__(self):
        return f'{self.unit.__full_str__()}: parent={self.parent}, ' \
               f'children={list(self.xml_element)}'

    def is_folder(self) -> bool:
        return self.unit.element_type == FOLDER_STR

    def is_file(self) -> bool:
        return self.unit.element_type == FILE_STR

    def is_import(self) -> bool:
        return self.unit.element_type == IMPORT_STR


def element_to_node(element: XMLElement, parent=None) -> ElementNode:
    return ElementNode(name=get_name(element),
                       element_type=get_element_type(element),
                       git_track=get_git_status(element),
                       parent=parent,
                       suffix=get_element_suffix(element),
                       element=element)


def generate(xml: XMLTree) -> Tree:
    def _folder_loop(node: ElementNode):
        print(f'LOOP: {node.unit.name}')
        for child in list(node.xml_element):
            _generate(child, node)

    def _generate(element: XMLElement, parent: ElementNode):
        '''if not element:
            raise Exception('No element was found')
            return'''

        print(f'_GENERATE element: ({element.tag}) parent: ({parent})')

        node = element_to_node(element=element, parent=parent)
        print(f'   generated node: {node.__full_str__()}')

        if node.is_folder():
            _folder_loop(node)

    root = ElementNode(xml.setup['name'],
                       element_type='folder',
                       git_track='true',
                       suffix='',
                       element=xml.root)
    tree = Tree(root)
    _folder_loop(tree.get_root())
    return tree
