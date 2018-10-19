from util.temp_handler import TempHandler
from models.model_parser import Tree
"""from util.git import GitHandler"""
from xml.etree.ElementTree import Element
from util.folders import WorkingDirectory


class Generator(object):
    def __init__(self, xml_location):
        self.tree = Tree(xml_location)
        """self.git_handler = GitHandler()"""
        self.temp_handler = TempHandler(self.tree.setup['name'],
                                        'Users/Michael')
        self.dir_stack = [None]

    def generate(self):
        self._generate(self.tree.root)
        self.temp_handler.finalize()
        return self.temp_handler.dir

    def _generate(self, cur: Element):
        print("called generate on: ", cur.tag)
        if not list(cur):
            print('BASE CASE FOUND AT: ', cur.tag)
            return

        '''for child in list(cur):'''
        item_type = str(cur.get('type'))

        if item_type == "folder":
            self._gen_dir(cur)
        elif item_type == "file":
            self._gen_file(cur)
        elif item_type == "autofile":
            self._gen_autofile(cur)
        else:
            raise Exception('invalid type: {}'.format(item_type))

    def _gen_dir(self, cur: Element):
        print("called generate directory for element: ", cur.tag)

        pushed = self.temp_handler.generate_dir(cur, self.dir_stack[-1])
        print('PUSHED: ', pushed)
        self.dir_stack.append(pushed)
        for child in list(cur):
            self._generate(child)

        popped = self.dir_stack.pop()
        print("POPPED: ", popped)

    def _gen_file(self, cur: Element):
        print("called generate file for element: ", cur.tag)
        file = self.temp_handler.generate_file(cur, self.dir_stack[-1])
        file.close()

    def _gen_autofile(self, cur: Element):
        print("called generate autofile for element: ", cur.tag)
        pass  # TODO
