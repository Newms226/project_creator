from models.element_node import ElementNode, element_to_node
from models.model_parser import XMLTree
from util.tree import Tree
from models import XMLElement


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

    def _generate(self, element: XMLElement, parent: ElementNode):
        '''if not element:
            raise Exception('No element was found')
            return'''

        print(f'_GENERATE element: ({element.tag}) parent: ({parent})')

        node = element_to_node(element=element, parent=parent)
        print(f'   generated node: {node.__full_str__()}')

        if node.is_folder():
            self._folder_loop(node)


if __name__ == '__main__':
    test = Generator('/Users/michael/prog/python/python3/project_creator/'
                     'design/examples/hierarchy_config.xml')
    test.generate()
