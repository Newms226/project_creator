import unittest
from src.parse.config import SimpleBuildConfig

class TestSimpleBuildConfig(unittest.TestCase):
    def setUp(self):
        self.config = SimpleBuildConfig('git', 'sync', 'folders', 'meta',
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

    def test_immutability(self):
        self.assertR