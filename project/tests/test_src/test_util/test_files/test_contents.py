import unittest
from src.util.files.contents import _prefix_handler

gen_texts = ['header',
             'header with new line\n',
             'many\nlines',
             'many\nlines\ no prefix/suffix'
             '\nmany lines \n with follow & precede\n']


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

    def test_with_rst_header(self):
        pass

    def test_rst_header_FALSE(self):
        pass

    def test_default_rst_char(self):
        pass

    def test_none_rst_char(self):
        pass

    def test_custom_rst_char(self):
        pass

    def test_with_overline(self):
        pass

    def test_without_overline(self):
        pass




if __name__ == '__main__':
    unittest.main()
