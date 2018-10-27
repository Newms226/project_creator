from models.element_node import ElementNode, element_to_node
from anytree import RenderTree
from models.model_parser import XMLTree
from xml.etree.ElementTree import Element
import models.config as config
from util.tree import Tree


class Generator(object):
    def __init__(self, xml_location):
        self.xml = XMLTree(xml_location)
        root = ElementNode(name=self.xml.setup['name'],
                           element_type='folder',
                           git_track='true',
                           suffix='',
                           element=self.xml.root)
        self.tree = Tree(root)

    def generate(self):
        self._folder_loop(self.tree.get_root())
        print(self.tree.__str__())

    def _folder_loop(self, node: ElementNode):
        print(f'LOOP: {node.unit.name}')
        for child in list(node.xml_element):
            self._generate(child, node)

    def _generate(self, element: Element, parent: ElementNode):
        '''if not element:
            raise Exception('No element was found')
            return'''

        print(f'_GENERATE element: ({element.tag}) parent: ({parent})')

        node = element_to_node(element=element, parent=parent)
        print(f'   generated node: {node}')

        t = node.unit.element_type
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
        self._folder_loop(node)

    def _generate_file(self, node: ElementNode):
        print(f' FILE: generating... {node}')
        # TODO generate file calls

    def _generate_import(self, node: ElementNode):
        print(f' IMPORT: generating... {node}')
        # TODO


if __name__ == '__main__':
    test = Generator('/Users/michael/prog/python/python3/project_creator/design/examples/hierarchy_config.xml')
    test.generate()