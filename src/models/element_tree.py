from models.element_node import ElementNode
from anytree import RenderTree
from models.model_parser import XMLTree


def tree_to_string(root: ElementNode) -> str:
    _str = ''

    for pre, _, node in RenderTree(root):
        _str += f'{pre}{node}\n'

    return _str


class TreeManager(object):
    def __init__(self, root: ElementNode):
        self.root = ElementNode

    def __str__(self):
        return tree_to_string(self.root)


class Generator(object):
    def __init__(self, xml_location):
        self.xml = XMLTree(xml_location)
        self._working_parent_node = ElementNode(name=self.xml.setup['name'],
                                                element_type='folder',
                                                git_track='true',
                                                suffix='')
        self.tree = TreeManager(root=self._working_parent_node)


    def generate(self):


    def _generate(self):

    def _generate_folder(self):

    def _generate_file(self):

    def _generate_import(self):
