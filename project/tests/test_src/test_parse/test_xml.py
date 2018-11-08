import unittest
from src.parse import XMLReader, XMLElement, XMLTree
from src.parse.xml import xml_to_tree_node, parse_contents


class TestXMLReader(unittest.TestCase):

    def setUp(self):
        self.folder_root: XMLElement = \
           XMLTree.parse('/Users/michael/prog/python/python3/project_creator'
                         '/project/tests/resources/basic_project.xml') \
           .getroot().find('folder_root')
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
        file = self.folder_root.find('design').find('agile')\
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
        self.folder_root: XMLElement = \
            XMLTree.parse('/Users/michael/prog/python/python3/project_creator'
                          '/project/tests/resources/basic_project.xml') \
                .getroot().find('folder_root')
        self.license = self.folder_root.find('LICENSE')
        self.backlog = self.folder_root.find('design').find('agile')\
            .find('sprint_backlog')
        self.src = self.folder_root.find('src')

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
        n = xml_to_tree_node(self.license, XMLReader)
        self.assertTrue(n is not None)
        self.assertTrue(n.name == 'LICENSE')
        self.assertTrue(n.parent is None)
        self.assertTrue(n.element == self.license)
        self.assertTrue(n.git_track is True)
        self.assertTrue(n.element_type == 'import')
        self.assertTrue(n.extension == 'rst')
        self.assertTrue(n.import_strategy == 'p')
        self.assertTrue(n.import_path == 'path/to/import')
        self.assertTrue(n.is_import())
        self.assertFalse(n.is_file())
        self.assertFalse(n.is_folder())

    def test_src_node(self):
        n = xml_to_tree_node(self.src, XMLReader)
        self.assertTrue(n is not None)
        self.assertTrue(n.name == 'src')
        self.assertTrue(n.parent is None)
        self.assertTrue(n.element == self.src)
        self.assertTrue(n.git_track is True)
        self.assertTrue(n.element_type == 'folder')
        self.assertFalse(n.is_import())
        self.assertFalse(n.is_file())
        self.assertTrue(n.is_folder())

    def test_sprint_backlog_node(self):
        n = xml_to_tree_node(self.backlog, XMLReader)
        self.assertTrue(n is not None)
        self.assertTrue(n.name == 'sprint_backlog')
        self.assertTrue(n.parent is None)
        self.assertTrue(n.element == self.backlog)
        self.assertTrue(n.git_track is False)
        self.assertTrue(n.element_type == 'file')
        self.assertTrue(n.extension == 'rst')
        self.assertTrue(n.header == 'Sprint Backlog')
        self.assertTrue(n.text == '#. design')
        self.assertFalse(n.is_import())
        self.assertTrue(n.is_file())
        self.assertFalse(n.is_folder())


if __name__ == '__main__':
    unittest.main()

