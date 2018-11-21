import unittest
from .context import src
from src.util.files.contents import _prefix_handler, \
    _generate_header_underline, \
    append_text, append_header, generate_file_text
from src.parse.xml_ import ImportNode
from parse.importer import parse

gen_texts = ['header',
             'header with new line\n',
             'many\nlines',
             'many\nlines\ no prefix/suffix'
             '\nmany lines \n with follow & precede\n']

test_file = '/Users/michael/prog/python/python3/src/test/' \
            'resources/file_parse_base.xml'


class TestPrefixHandler(unittest.TestCase):

    def setUp(self):
        self.gen_texts = gen_texts

    def test_none_passed(self):
        with self.assertRaises(TypeError):
            _prefix_handler(append_to=None, generated_text=None)

    def test_empty(self):
        self._helper('')

    def test_one_line(self):
        self._helper('one line')

    def test_many_lines(self):
        self._helper('on\nlots\nof\nlines')

    def test_trailing_new_line(self):
        self._helper('with trailing new line \n')

    def _helper(self, append_to):
        for text in self.gen_texts:
            with self.subTest():
                returned = _prefix_handler(append_to=append_to,
                                           generated_text=text)
                exp = append_to + '\n' + text
                self.assertMultiLineEqual(exp, returned)
                self.assertEqual(exp, returned)


class TestHeader(unittest.TestCase):
    def setUp(self):
        self.contents = gen_texts
        self.headers = ['HEADER', 'Dumb header\n']
        self.chars = ['#', '=', 'a', '_']

    def test_underline_gen(self):
        for header in self.headers:
            with self.subTest():
                returned = _generate_header_underline(header)
                self.assertTrue(len(returned) == len(header) + 1)

    def test_with_rst_header(self):
        for header in self.headers:
            with self.subTest():
                underline = _generate_header_underline(header)
                exp = header + '\n' + underline
                self.assertEqual(exp, append_header(header_contents=header,
                                                    prefix_new_line=False))

        for append_to in self.contents:
            for header in self.headers:
                with self.subTest():
                    underline = _generate_header_underline(header)
                    exp = append_to + '\n' + header + '\n' + underline
                    self.assertEqual(exp, append_header(header_contents=header,
                                                        append_to=append_to,
                                                        prefix_new_line=True))

    def test_without_rst_header(self):
        for append_to in self.contents:
            for header in self.headers:
                with self.subTest():
                    self.assertEqual(append_to + header,
                                     append_header(header_contents=header,
                                                   append_to=append_to,
                                                   rst_header=False,
                                                   prefix_new_line=False))

        for append_to in self.contents:
            for header in self.headers:
                with self.subTest():
                    self.assertEqual(append_to + '\n' + header,
                                     append_header(header_contents=header,
                                                   append_to=append_to,
                                                   rst_header=False))

    def test_rst_char(self):
        with self.assertRaises(Exception):
            _generate_header_underline(header='x', header_char='xx')
            _generate_header_underline(header=None)
            _generate_header_underline(header='x', header_char=None)
            _generate_header_underline(None, None)

        for char in self.chars:
            for header in self.headers:
                with self.subTest():
                    returned = _generate_header_underline(header=header,
                                                          header_char=char)
                    self.assertTrue(len(returned) == len(header) + 1)

    def test_with_overline(self):
        for char in self.chars:
            for append_to in self.contents:
                for header in self.headers:
                    with self.subTest():
                        underline = _generate_header_underline(
                            header=header, header_char=char)
                        exp = append_to + '\n' + underline + '\n' + header \
                              + '\n' + underline
                        self.assertEqual(exp,
                                         append_header(header_contents=header,
                                                       append_to=append_to,
                                                       overline=True,
                                                       rst_char=char))


class TestText(unittest.TestCase):
    def setUp(self):
        self.contents = gen_texts
        self.texts = gen_texts

    def test_no_new_line(self):
        for append_to in self.contents:
            for text in self.texts:
                with self.subTest():
                    exp = append_to + text
                    self.assertEqual(exp, append_text(text=text,
                                                      append_to=append_to,
                                                      prefix_new_line=False))

    def test_new_line(self):
        for append_to in self.contents:
            for text in self.texts:
                with self.subTest():
                    exp = append_to + '\n' + text
                    self.assertEqual(exp, append_text(text=text,
                                                      append_to=append_to,
                                                      prefix_new_line=True))


class TestImportNodeParse(unittest.TestCase):
    def setUp(self):
        self.folder_node = None
        config = parse(test_file)
        root: ImportNode = config.folder_hierarchy.get_root()
        agile = root.get_child('design').get_child('agile')
        self.project_backlog = agile.get_child('project_backlog')
        self.sprint_backlog = agile.get_child('sprint_backlog')
        self.readme = root.get_child('README')
        self.license = root.get_child('LICENSE')
        # print(config.folder_hierarchy)

    def test_project_backlog(self):
        self.assertTrue(self.project_backlog is not None)
        self.assertTrue(type(self.project_backlog) is ImportNode)
        self._helper(exp='Project Backlog\n================',
                     node=self.project_backlog)

    def test_sprint_backlog(self):
        self.assertTrue(self.sprint_backlog is not None)
        print(type(self.sprint_backlog))
        self.assertTrue(type(self.sprint_backlog) is ImportNode)

        self._helper(node=self.sprint_backlog,
                     exp='Sprint Backlog\n===============\n#. design',
                     prefix_new_line=True)

    def test_readme(self):
        self.assertTrue(self.readme is not None)
        self.assertTrue(type(self.readme) is ImportNode)
        self._helper(node=self.readme,
                     exp='Readme\n=======\nThis is the readme',
                     prefix_new_line=True)

    def test_license(self):
        self.assertTrue(self.license is not None)
        self.assertTrue(type(self.license) is ImportNode)
        self._helper(node=self.license,
                     exp='License\n========',
                     prefix_new_line=True)

    def _helper(self, node, exp, prefix_new_line=False):
        self.assertEqual(exp,
                         generate_file_text(file_node=node,
                                            prefix_new_line=prefix_new_line))


if __name__ == '__main__':
    unittest.main()
