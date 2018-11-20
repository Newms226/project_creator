from .context import src
import unittest

from parse import FileTree
from model.node import ImportNode


class TestImportNode(unittest.TestCase):

    def setUp(self):
        self.names = ['valid', 'still_valid', 'spaced out']
        self.types = ['file', 'folder']
        self.tracks = [True, False]

    def test_properties(self):
        for name in self.names:
            for type_ in self.types:
                for track in self.tracks:
                    with self.subTest():
                        n = ImportNode(name=name,
                                       element_type=type_,
                                       git_track=track)
                        self.assertEqual(name, n.name)
                        self.assertEqual(type_, n.element_type)
                        self.assertEqual(track, n.git_track)

                        with self.assertRaises(AttributeError):
                            n.name = 'asdfas'
                            n.git_track = False
                            n.element_type = 'asdfaswga'
                            n.name = False
                            n.element_type = True
                            n.git_track = 'asdfasdf'

    def test_type_bools(self):
        n = ImportNode('name', 'folder', True)
        self.assertTrue(n.is_folder())
        self.assertFalse(n.is_file())

        n = ImportNode('name', 'file', True)
        self.assertFalse(n.is_folder())
        self.assertTrue(n.is_file())

    def test_get_child(self):
        root = ImportNode('root', 'folder', True)
        a = ImportNode('r_a', 'folder', True, parent=root)
        b = ImportNode('r_b', 'folder', True, parent=root)
        a_a = ImportNode('r_a_a', 'folder', True, parent=a)

        self.assertEqual(a, root.get_child('r_a'))
        self.assertEqual(b, root.get_child('r_b'))
        self.assertTrue(root.get_child('r_a_a') is None)
        self.assertEqual(a_a, root.get_child('r_a_a', 3))
        self.assertEqual(a_a, a.get_child('r_a_a'))

    def test_contains(self):
        root = ImportNode('root', 'folder', True)
        a = ImportNode('r_a', 'folder', True, parent=root)
        b = ImportNode('r_b', 'folder', True, parent=root)
        a_a = ImportNode('r_a_a', 'folder', True, parent=a)

        self.assertTrue(a in root)
        self.assertFalse(a_a in root)
        self.assertTrue(root.__contains__(item=a_a, max_level=3))


class TestFileTree(unittest.TestCase):

    def setUp(self):
        self.root = ImportNode('root', 'folder', True)
        a = ImportNode('r_a', 'folder', True, parent=self.root)
        b = ImportNode('r_b', 'folder', True, parent=self.root)
        a_a = ImportNode('r_a_a', 'folder', True, parent=a)
        self.tree = FileTree(root=self.root)

    def test_count(self):
        self.assertEqual(3, self.tree.node_count)

    def test_root(self):
        self.assertEqual(self.root, self.tree.get_root())



