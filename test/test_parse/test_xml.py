import unittest

from src.extensions import XMLElement, XMLTree
from src.parse.xml_ import XML_READER, XMLTreeReader
from src.parse.importer import parse
from test import INFO, ELEMENTS


def gen_elements(elements):
    def find(root, key: str):
        levels = list(key.split('/'))
        for level in levels:
            root = root.find(level)
        return root

    for data in elements:
        root = XMLTree.parse(data['path']).getroot()
        for k, v in data['elements'].items():
            node = find(root, k)
            yield v, node


class TestXMLReader(unittest.TestCase):

    def setUp(self):
        self.reader = XML_READER

    def test_parse(self):
        for v, node in gen_elements(ELEMENTS):
            with self.subTest():
                self.assertTrue(v is not None)
                self.assertTrue(node is not None)

    def test_git_read(self):
        for v, node in gen_elements(ELEMENTS):
            with self.subTest():
                self.assertEqual(v['git'], self.reader.git_track(node))

    def test_type(self):
        for v, node in gen_elements(ELEMENTS):
            with self.subTest():
                self.assertEqual(v['type'], self.reader.element_type(node))

    def test_name(self):
        for v, node in gen_elements(ELEMENTS):
            with self.subTest():
                self.assertEqual(v['name'], self.reader.name(node))

    def test_parse_element_contents(self):
        for v, node in gen_elements(ELEMENTS):
            with self.subTest():
                parsed = self.reader.parse_contents(node, require_folder=False)

                if 'text' in v:
                    self.assertEqual(v['text'], parsed['text'])

                if 'header' in v:
                    self.assertEqual(v['header'], parsed['header'])

                if 'extension' in v:
                    self.assertEqual(v['extension'], parsed['extension'])

    def test_children(self):
        for v, node in gen_elements(ELEMENTS):
            with self.subTest():
                if 'children' in v:
                    read = [child.tag for child in self.reader.children(node)]
                    self.assertEqual(v['children'], read)


class TestXMLTreeReader(unittest.TestCase):

    def setUp(self):
        self.reader = XML_READER

    def test_parse_info_contents(self):
        for v, node in gen_elements(INFO):
            with self.subTest():
                parsed = self.reader.parse_contents(node,
                                                    require_folder=False)
                for k, _ in v.items():
                    self.assertEqual(v[k], parsed[k])


