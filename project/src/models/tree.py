from anytree import RenderTree, NodeMixin

from models import FOLDER_TYPE, FILE_TYPE, IMPORT_TYPE, NodeBase, XMLElement
from models.xml_parser import Unit, get_name, get_element_type, get_git_status, \
    get_element_suffix, XMLTree


def tree_to_string(root: NodeMixin) -> str:
    _str = ''

    for pre, _, node in RenderTree(root):
        _str += f'{pre}{node}\n'

    return _str


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
        return self.unit.element_type == FOLDER_TYPE

    def is_file(self) -> bool:
        return self.unit.element_type == FILE_TYPE

    def is_import(self) -> bool:
        return self.unit.element_type == IMPORT_TYPE


class FileNode(ElementNode):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, element: XMLElement, parent: NodeBase = None):
        if element_type != FILE_TYPE:
            raise Exception(f'Attempted to make file node {name} when the '
                            f'element type was {element_type}')

        ElementNode.__init__(self, name=name, element_type=element_type,
                             git_track=git_track, suffix=suffix,
                             element=element, parent=parent)

    def is_file(self) -> bool: return True

    def is_folder(self) -> bool: return False

    def is_import(self) -> bool: return False


class FolderNode(ElementNode):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, element: XMLElement, parent: NodeBase = None):
        if element_type != FOLDER_TYPE:
            raise Exception(f'Attempted to make folder node {name} when the '
                            f'element type was {element_type}')

        ElementNode.__init__(self, name=name, element_type=element_type,
                             git_track=git_track, suffix=suffix,
                             element=element, parent=parent)

    def is_file(self) -> bool: return False

    def is_folder(self) -> bool: return True

    def is_import(self) -> bool: return False


class ImportNode(ElementNode):
    def __init__(self, name: str, element_type: str, git_track: bool,
                 suffix: str, element: XMLElement, parent: NodeBase = None):
        if element_type != IMPORT_TYPE:
            raise Exception(f'Attempted to make parse node {name} when the '
                            f'element type was {element_type}')

        ElementNode.__init__(self, name=name, element_type=element_type,
                             git_track=git_track, suffix=suffix,
                             element=element, parent=parent)

    def is_file(self) -> bool: return False

    def is_folder(self) -> bool: return False

    def is_import(self) -> bool: return True


def element_to_node(element: XMLElement, parent=None) -> ElementNode:
    type_ = get_element_type(element)
    if type_ == FOLDER_TYPE:
        return FolderNode(name=get_name(element),
                          element_type=type_,
                          git_track=get_git_status(element),
                          parent=parent,
                          suffix=get_element_suffix(element),
                          element=element)
    elif type_ == FILE_TYPE:
        return FileNode(name=get_name(element),
                        element_type=type_,
                        git_track=get_git_status(element),
                        parent=parent,
                        suffix=get_element_suffix(element),
                        element=element)
    elif type_ == IMPORT_TYPE:
        return ImportNode(name=get_name(element),
                          element_type=type_,
                          git_track=get_git_status(element),
                          parent=parent,
                          suffix=get_element_suffix(element),
                          element=element)
    else:
        raise Exception(f'Element did not have a valid type: {type_} @ '
                        f'{element}')


class Tree(object):

    def __init__(self, root_node: NodeMixin): self.root = root_node

    def get_root(self) -> ElementNode: return self.root

    def get_rendered_tree(self): return RenderTree(self.root)

    def __str__(self): return tree_to_string(self.root)


def generate_tree(xml: XMLTree) -> Tree:
    def _folder_loop(node: ElementNode):
        print(f'LOOP: {node.unit.name}')
        for child in list(node.xml_element):
            _generate(child, node)

    def _generate(element: XMLElement, parent: ElementNode):
        if element is None:
            raise Exception('No element was found')
            return

        print(f'_GENERATE element: ({element.tag}) parent: ({parent})')

        node = element_to_node(element=element, parent=parent)
        print(f'   generated node: {node.__full_str__()}')

        if node.is_folder():
            _folder_loop(node)

    root = ElementNode(xml.setup['name'],
                       element_type='folder',
                       git_track='true',
                       suffix='',
                       element=xml.folder_root)
    tree = Tree(root)
    _folder_loop(tree.get_root())
    return tree
