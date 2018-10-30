from models import XMLTree, generate_tree, ElementNode
from util import WorkingDirectory, TempHandler, make_folder, make_file
from os import path


class Generator(object):
    def __init__(self, xml_location):
        self.xml = XMLTree(xml_location)
        '''self.git_handler = GitTracker()'''
        self.temp_handler = TempHandler(self.xml.setup['root_dir'])
        self.working_dir = WorkingDirectory(root=self.temp_handler.dir)
        self.tree = generate_tree(self.xml)

    def generate(self):
        for child in list(self.tree.get_root().children):
            self._generate(child)

        self.temp_handler.finalize()

    def _generate(self, cur: ElementNode):
        print(f'Called _generate({cur.unit.name}) w/ type '
              f'{cur.unit.element_type}')

        if cur.is_folder():
            self._gen_dir(cur)
        elif cur.is_file():
            self._gen_file(cur)
        elif cur.is_import():
            self._gen_import(cur)
        else:
            raise Exception(f'invalid type: {cur.unit.element_type}')

    def _gen_dir(self, cur: ElementNode):
        print(f' called _gen_dir({cur.unit.name}')

        self.working_dir.push(cur.unit.name)
        make_folder(self.working_dir.absolute_dir)

        '''self.git_handler.register(cur, self.working_dir.relative_dir)'''

        for child in list(cur.children):
            self._generate(child)

        self.working_dir.pop()
        print(f'END LOOP: {cur.unit.name} is done.')

    def _gen_file(self, cur: ElementNode):
        print(f' called generate file for element: {cur.unit.name}')

        make_file(path=self.working_dir.absolute_dir,
                  name=cur.unit.name,
                  suffix=cur.unit.suffix)

        '''self.git_handler.register(cur, self.working_dir.relative_dir + '/' +
                                  _filename)'''

    def _gen_import(self, cur: ElementNode):
        print(f' called generate import as {cur.unit.name}')
        pass  # TODO


if __name__ == '__main__':
    tester = Generator('/Users/michael/prog/python/python3/project_creator/'
                       'design/examples/hierarchy_config.xml')
    tester.generate()