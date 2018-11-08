import unittest
from src.parse import XMLReader, XMLElement, XMLTree
from src.parse.xml import parse_contents


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


class TestParseContents(unittest.TestCase):
    def setUp(self):
        self.folder_root: XMLElement = \
            XMLTree.parse('/Users/michael/prog/python/python3/project_creator'
                          '/project/tests/resources/basic_project.xml') \
                .getroot().find('folder_root')
        self.license = self.folder_root.find('LICENSE')
        self.backlog = self.folder_root.find('design').find('agile')\
            .find('sprint_backlog')

    def test_license(self):
        d = parse_contents(self.license, XMLReader, False)
        self.assertTrue(d is not None)
        self.assertTrue(d['path'] == 'resources/MIT.rst')
        self.assertTrue(d['extension'] == 'rst')
        self.assertTrue(d['import_strategy'] == 'p')
        self.assertTrue(d['import_path'] == 'path/to/import')

    def test_backlog(self):
        d = parse_contents(self.backlog, XMLReader, False)
        self.assertTrue(d is not None)
        self.assertTrue(d['extension'] == 'rst')
        self.assertTrue(d['header'] == 'Sprint Backlog')
        self.assertTrue(d['text'] == '#. design')


if __name__ == '__main__':
    unittest.main

