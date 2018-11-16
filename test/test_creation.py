import unittest, tempfile
from .context import project_creator
from project_creator.util.files.creation import gen_file_name, \
    _get_valid_name, write_file_text
from project_creator.parse.xml_ import parse

test_file = '/Users/michael/prog/python/python3/project_creator/test' \
            '/resources/file_parse_base.xml'


class TestGenFileName(unittest.TestCase):
    def setUp(self):
        self.separators = ['/', '.', '_']
        self.names = ['readme', 'license', 'CONTRIB', 'Sp ace', '0Digit']
        self.extensions = ['rst', 'md', 'py']
        self.locations = ['path/to', 'path', 'path_to/location']

    def test_name_gen(self):
        def _helper(exp, text):
            self.assertEqual(exp, _get_valid_name(text))

        _helper('readme', 'readme')
        _helper('contrib', 'CONTRIB')
        _helper('sp_ace', 'Sp ace')
        _helper('_0digit', '0Digit')

    def test_simple(self):
        for name in self.names:
            for ext in self.extensions:
                with self.subTest():
                    exp = _get_valid_name(name) + '.' + ext
                    result = gen_file_name(name=name,
                                           extension=ext)
                    self.assertEqual(exp, result)

    def test_complex(self):
        for name in self.names:
            for ext in self.extensions:
                for sep in self.separators:
                    with self.subTest():
                        exp = _get_valid_name(name) + sep + ext
                        result = gen_file_name(name=name,
                                               extension=ext,
                                               file_separator=sep)
                        self.assertEqual(exp, result)

    def test_following_sep(self):
        for location in self.locations:
            for name in self.names:
                for exten in self.extensions:
                    with self.subTest():
                        exp = location + '/' + _get_valid_name(name) + '.' + \
                              exten
                        result = gen_file_name(name=name,
                                               extension=exten,
                                               location=location + '/')
                        self.assertEqual(exp, result)

    def test_location(self):
        for location in self.locations:
            for name in self.names:
                for exten in self.extensions:
                    with self.subTest():
                        exp = location + '/' + _get_valid_name(name) + '.' + \
                              exten
                        result = gen_file_name(name=name,
                                               extension=exten,
                                               location=location)
                        self.assertEqual(exp, result)


class TestFileWrite(unittest.TestCase):

    def setUp(self):
        self.config = parse(test_file)
        root: ImportNode = self.config.folder_hierarchy.get_root()
        agile = root.get_child('design').get_child('agile')
        self.location = tempfile.mkdtemp()

        self.expected = {
            'license': {
                'node': root.get_child('LICENSE'),
                'expected': 'License\n========'
            },
            'sprint_backlog': {
                'node': agile.get_child('sprint_backlog'),
                'expected': 'Sprint Backlog\n===============\n#. design'
            },
            'readme': {
                'node': root.get_child('README'),
                'expected': 'Readme\n=======\nThis is the readme'
            },
            'project_backlog': {
                'node': agile.get_child('project_backlog'),
                'expected': 'Project Backlog\n================'
            }
        }

    def test_write(self):
        d = self.expected
        for test in list(d):
            with self.subTest():
                path_ = write_file_text(file_node=d[test]['node'],
                                        location=self.location)
                # print(path_)

                with open(path_, 'r') as f:
                    out = f.read()
                    f.close()

                self.assertEqual(d[test]['expected'], out)



if __name__ == '__main__':
    unittest.main()
