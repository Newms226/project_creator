from manager import Generator
import unittest


class TestManager(unittest.TestCase):
    def setUp(self):
        self.test = Generator('/Users/michael/prog/python/python3/'
                              'project_creator/design/examples/'
                              'hierarchy_config.xml')

    def test_generator(self):
        self.test.generate()
