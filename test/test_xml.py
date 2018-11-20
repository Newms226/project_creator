import unittest
from .context import src
from src.parse.xml_ import XMLReader, XMLElement, XMLTree
from model.node import ImportNode
from src.parse.xml_ import parse_contents
from parse.importer import to_tree_node, generate_tree, parse

test_file = '/Users/michael/prog/python/python3/src/test/' \
            'resources/basic_project.xml'


class TestXMLReader(unittest.TestCase):

    def setUp(self):
        self.folder_root: XMLElement = \
            XMLTree.parse(test_file).getroot().find('folder_root')
        self.reader = XMLReader

    def test_tracked_folder(self):
        folder = self.folder_root.find('src')
        self.assertTrue(folder is not None)
        self.assertTrue(self.reader.git_track(folder) is True)
        self.assertTrue(self.reader.element_type(folder) == 'folder')
        self.assertTrue(self.reader.name(folder) == 'src')

    def test_untracked_folder(self):
        folder = self.folder_root.find('venv')
        self.assertTrue(folder is not None)
        self.assertTrue(self.reader.git_track(folder) is False)
        self.assertTrue(self.reader.element_type(folder) == 'folder')
        self.assertTrue(self.reader.name(folder) == 'venv')

    def test_tracked_file(self):
        file = self.folder_root.find('README')
        self.assertTrue(file is not None)
        self.assertTrue(self.reader.git_track(file) is True)
        self.assertTrue(self.reader.element_type(file) == 'file')
        self.assertTrue(self.reader.name(file) == 'README')

    def test_untracked_file(self):
        file = self.folder_root.find('design').find('agile') \
            .find('sprint_backlog')
        self.assertTrue(file is not None)
        self.assertTrue(self.reader.git_track(file) is False)
        self.assertTrue(self.reader.element_type(file) == 'file')
        self.assertTrue(self.reader.name(file) == 'sprint_backlog')

    def test_import(self):
        import_ = self.folder_root.find('LICENSE')
        self.assertTrue(import_ is not None)
        self.assertTrue(self.reader.git_track(import_) is True)
        self.assertTrue(self.reader.element_type(import_) == 'import')
        self.assertTrue(self.reader.name(import_) == 'LICENSE')


class TestParseElement(unittest.TestCase):
    def setUp(self):
        self.tree_root = XMLTree.parse(test_file).getroot()
        self.folder_root: XMLElement = self.tree_root.find('folder_root')
        self.license = self.folder_root.find('LICENSE')
        self.backlog = self.folder_root.find('design').find('agile') \
            .find('sprint_backlog')
        self.src = self.folder_root.find('src')

    def test_parse_info(self):
        d = parse_contents(self.tree_root.find('meta'))
        self.assertTrue(d is not None)
        self.assertTrue(d['name'] == 'Project Creator')
        self.assertTrue(d['root_dir'] == '/Users/Michael/prog/python/python3')
        self.assertTrue(d['date']['month'] == '10')
        self.assertTrue(d['date']['day'] == '5')
        self.assertTrue(d['date']['year'] == '2018')
        self.assertTrue(d['license'] == 'MIT')
        self.assertTrue(d['short_description'] is None)
        self.assertTrue(d['long_description'] is None)
        self.assertTrue(d[
                            'contributors'] == 'Michael Newman, OTHER CONTR., COMMA SEPARATED')

    def test_license_dict_parse(self):
        d = parse_contents(self.license, XMLReader, False)
        self.assertTrue(d is not None)
        self.assertTrue(d['path'] == 'resources/MIT.rst')
        self.assertTrue(d['extension'] == 'rst')
        self.assertTrue(d['import_strategy'] == 'p')
        self.assertTrue(d['import_path'] == 'path/to/import')

    def test_backlog_dict_parse(self):
        d = parse_contents(self.backlog, XMLReader, False)
        self.assertTrue(d is not None)
        self.assertTrue(d['extension'] == 'rst')
        self.assertTrue(d['header'] == 'Sprint Backlog')
        self.assertTrue(d['text'] == '#. design')

    def test_license_node(self):
        n = to_tree_node(self.license, XMLReader)
        self.assertTrue(n is not None)
        self.assertTrue(n.name == 'LICENSE')
        self.assertTrue(n.parent is None)
        self.assertTrue(n.git_track is True)
        self.assertTrue(n.element_type == 'import')
        self.assertTrue(n.extension == 'rst')
        self.assertTrue(n.import_strategy == 'p')
        self.assertTrue(n.import_path == 'path/to/import')
        self.assertFalse(n.is_file())
        self.assertFalse(n.is_folder())

    def test_src_node(self):
        n = to_tree_node(self.src, XMLReader)
        self.assertTrue(n is not None)
        self.assertTrue(n.name == 'src')
        self.assertTrue(n.parent is None)
        self.assertTrue(n.git_track is True)
        self.assertTrue(n.element_type == 'folder')
        self.assertFalse(n.is_file())
        self.assertTrue(n.is_folder())

    def test_sprint_backlog_node(self):
        n = to_tree_node(self.backlog, XMLReader)
        self.assertTrue(n is not None)
        self.assertTrue(n.name == 'sprint_backlog')
        self.assertTrue(n.parent is None)
        self.assertTrue(n.git_track is False)
        self.assertTrue(n.element_type == 'file')
        self.assertTrue(n.extension == 'rst')
        self.assertTrue(n.header == 'Sprint Backlog')
        self.assertTrue(n.text == '#. design')
        self.assertTrue(n.is_file())
        self.assertFalse(n.is_folder())


class TestTreeParse(unittest.TestCase):
    def setUp(self):
        self.root = XMLTree.parse(test_file).getroot()
        self.tree = generate_tree(self.root, 'test')

    def test_count(self):
        self.assertTrue(self.tree.node_count == 12)

    def test_count_set(self):
        with self.assertRaises(AttributeError):
            self.tree.node_count = 20
        self.assertTrue(self.tree.node_count == 12)

    def test_count_del(self):
        with self.assertRaises(AttributeError):
            del self.tree.node_count
        self.assertTrue(self.tree.node_count == 12)

    def test_print(self):
        self.assertTrue(self.tree.__str__() is not None)
        self.assertTrue(self.tree.__str__(detail=10) is not None)
        self.assertTrue(self.tree.__str__(detail=5) is not None)

    def test_root_children(self):
        self.assertTrue(self.tree.get_root().get_child('src') is not None)
        self.assertTrue(self.tree.get_root().get_child('test') is not None)
        self.assertTrue(self.tree.get_root().get_child('design') is not None)
        self.assertTrue(self.tree.get_root().get_child('venv') is not None)
        self.assertTrue(self.tree.get_root().get_child('README') is not None)
        self.assertTrue(self.tree.get_root().get_child('LICENSE') is not None)

    def test_find_child(self):
        self.assertTrue(self.tree.get_root().get_child('src').name == 'src')
        self.assertTrue(self.tree.get_root().get_child('agile') is None)
        self.assertTrue(self.tree.get_root().get_child('agile', max_level=3)
                        is not None)

    def test_design_children(self):
        exp = (ImportNode(name='agile', element_type='folder', git_track=True),
               ImportNode(name='examples', element_type='folder',
                          git_track=True),
               ImportNode(name='strategy', element_type='folder',
                          git_track=True))
        design = self.tree.get_root().get_child('design')
        self.assertTrue(design is not None)
        self.assertTrue(design.get_child('agile') is not None)
        self.assertTrue(design.get_child('examples') is not None)
        self.assertTrue(design.get_child('strategy') is not None)

    def test_contains(self):
        design = self.tree.get_root().get_child('design')
        self.assertTrue(design in self.tree.get_root())


class TestFullParse(unittest.TestCase):
    def setUp(self):
        self.parsed = parse(file_=test_file)

    def test_parsed(self):
        self.assertTrue(self.parsed is not None)

    def test_metadata_parse(self):
        self.assertTrue(self.parsed.metadata is not None)
        self.assertTrue(self.parsed.metadata['name'] == 'Project Creator')
        self.assertTrue(self.parsed.metadata['root_dir']
                        == '/Users/Michael/prog/python/python3')
        self.assertTrue(self.parsed.metadata['license'] == 'MIT')

    def test_language_parse(self):
        l = self.parsed.language
        self.assertTrue(l is not None)
        self.assertTrue(l['type'] == 'Python')
        self.assertTrue(l['version'] == '3.7')
        self.assertTrue(
            l['requirements'] == 'anytree, comma_seperated_list, unittest')
        self.assertTrue(l['frameworks'] is None)

    def test_folder(self):
        f = self.parsed.folder_hierarchy
        self.assertTrue(f is not None)
        root = f.get_root()
        self.assertTrue(root is not None)
        self.assertTrue(root.get_child('src') is not None)
        self.assertTrue(root.get_child('tests') is not None)
        self.assertTrue(root.get_child('design') is not None)
        self.assertTrue(root.get_child('venv') is not None)
        self.assertTrue(root.get_child('README') is not None)
        self.assertTrue(root.get_child('LICENSE') is not None)


if __name__ == '__main__':
    unittest.main()
