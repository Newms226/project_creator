import unittest
from .context import project_creator
from project_creator.util.immutable_tuple import ImmutableConfig


class TestStringConfig(unittest.TestCase):
    def setUp(self):
        self.config = ImmutableConfig('git', 'sync', 'folders', 'meta',
                                      'language', 'auto generate',
                                      'execution', 'security')

    def test_git_contents(self):
        self.assertTrue(self.config.git == 'git')

    def test_sync_contents(self):
        self.assertTrue(self.config.sync == 'sync')

    def test_folders_contents(self):
        self.assertTrue(self.config.folder_hierarchy == 'folders')

    def test_meta_contents(self):
        self.assertTrue(self.config.metadata == 'meta')

    def test_language_contents(self):
        self.assertTrue(self.config.language == 'language')

    def test_auto_contents(self):
        self.assertTrue(self.config.auto_generate == 'auto generate')

    def test_execution_contents(self):
        self.assertTrue(self.config.execution == 'execution')

    def test_security_contents(self):
        self.assertTrue(self.config.security == 'security')

    def test_replace_fail(self):
        with self.assertRaises(Exception):
            self.config._replace()

    def test_set_fail(self):
        with self.assertRaises(AttributeError):
            self.config.git = 'FAIL'

    def test_size(self):
        self.assertTrue(len(self.config) == 8)

    def test_dict_len_empty(self):
        self.assertTrue(len(self.config.__dict__) == 0)

    def test_dict_empty(self):
        self.assertTrue(self.config.__dict__ == {})


if __name__ == '__main__':
    unittest.main()
