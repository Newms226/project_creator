from models.element_node import ElementNode, element_to_node
from anytree import RenderTree
from models.model_parser import XMLTree
from xml.etree.ElementTree import Element
import models.config as config



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
        self._generate_loop(self._working_parent_node)
        print(tree_to_string(self._working_parent_node))

    def _generate_loop(self, node: ElementNode):
        print(f'LOOP: {node.unit.name}')
        for child in list(node.xml_element):
            self._generate(child, node)

    def _generate(self, element: Element, parent: ElementNode):
        if not element:
            raise Exception('No element was found')
            return

        print(f'_GENERATE element: ({element.tag}) parent: ({parent})')

        node = element_to_node(element=element, parent=parent)
        with node.unit.element_type as t:
            if t == config.FILE_STR:
                self._generate_file(node)
            elif t == config.FOLDER_STR:
                self._generate_folder(node)
            elif t == config.IMPORT_STR:
                self._generate_import(node)
            else:
                raise Exception(f'Could not parse {node}')

    def _generate_folder(self, node: ElementNode):
        print(f' FOLDER: generating... {node}')

        # TODO generate folder calls
        self._generate_loop(node)


    def _generate_file(self, node: ElementNode):
        print(f' FILE: generating... {node}')
        # TODO generate file calls

    def _generate_import(self, node: ElementNode):
        print(f' IMPORT: generating... {node}')
        # TODO
