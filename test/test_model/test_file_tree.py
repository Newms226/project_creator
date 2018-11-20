import unittest

from src.model.file_tree import FileTree
from src.model.node import ImportNode


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
        self.assertEqual(self.root, self.tree.root)
