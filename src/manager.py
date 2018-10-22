from util.paths import TempHandler
from models.model_parser import Tree
from util.git import GitTracker
from xml.etree.ElementTree import Element
from util.folders import WorkingDirectory, make_dir
from os import path as Paths


class Generator(object):
    def __init__(self, xml_location):
        self.xml = Tree(xml_location)
        self.git_handler = GitTracker()
        self.temp_handler = TempHandler(self.xml.setup['root_dir'])
        self.working_dir = WorkingDirectory(root=self.temp_handler.dir)

    def generate(self):
        for child in list(self.xml.root):
            self._generate(child)

        self.temp_handler.finalize()

    def _generate(self, cur: Element):
        item_type = str(cur.get('type'))
        print(f'Called _generate({cur.tag}) w/ type {item_type}')

        if item_type == "folder":
            self._gen_dir(cur)
        elif item_type == "file":
            self._gen_file(cur)
        elif item_type == "autofile":
            self._gen_autofile(cur)
        else:
            raise Exception(f'invalid type: {item_type}')

    def _gen_dir(self, cur: Element):
        print(f' called _gen_dir({cur.tag}')

        self.working_dir.push(cur.tag)
        make_dir(self.working_dir.absolute_dir)
        for child in list(cur):
            self._generate(child)

        self.working_dir.pop()
        print(f'END LOOP: {cur.tag} is done.')

    def _gen_file(self, cur: Element):
        print(f' called generate file for element: {cur.tag}')

        _ext = cur.findtext('extension')
        if not _ext:
            print(f' WARNING: found no extension for {cur.tag}')
            _filename = cur.tag
        else:
            _filename = cur.tag + '.' + _ext
            print(f'  _filename = {_filename}')

        _path = Paths.join(self.working_dir.absolute_dir, _filename)
        print(f' _path relativized as {_path}')
        open(_path, 'w+').close()  # TODO Text import, etc.

    def _gen_autofile(self, cur: Element):
        print(" called generate autofile for element: ", cur.tag)
        pass  # TODO
