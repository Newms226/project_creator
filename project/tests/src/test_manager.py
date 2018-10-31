from project.src import Generator
import unittest


class TestManager(unittest.TestCase):
    def setUp(self):
        self.test = Generator('/Users/michael/prog/python/python3/'
                              'project_creator/tests/resources/creation_test_1/'
                              'hierarchy_config.xml')

    def test_generator_doesnt_fail(self):
        self.test.generate()


if __name__ == '__main__':
    unittest.main()
