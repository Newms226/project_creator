import unittest
import tempfile
from ast import literal_eval
from .context import src
from src.util.templates import parse_template

tests = [
    {
        'template': 'This is a \nmulti-line string with a \n variable $NAME '
                    'and another var $YEAR',
        'args': "YEAR=2018, NAME='Michael Newman'",
        'expected': 'This is a \nmulti-line string with a \n variable '
                    'Michael Newman and another var 2018'
    },
    {
        'template': 'This is a \nmulti-line string with a \n variable $NAME '
                    'and another var $YEAR',
        'args': "YEAR=2018",
        'expected': 'This is a \nmulti-line string with a \n variable '
                    '$NAME and another var 2018'
    }
]

fails = [
    {
        'template': 'This is a \nmulti-line string with a \n variable '
                    '$NAME and another var $YEAR',
        'args': "",
        'expected': 'This is a \nmulti-line string with a \n variable '
                    '$NAME and another var 2018',
        'type': ValueError
    },
    {
        'template': 'This is a \nmulti-line string with a \n variable '
                    '$NAME and another var $YEAR',
        'args': "",
        'expected': 'This is a \nmulti-line string with a \n variable '
                    '$NAME and another var 2018',
        'type': ValueError
    }
]


templates = ['This is a \nmulti-line string witha \n variable $NAME \n '
             'and another var $YEAR',
             'NO VARIABLES CONTAINED',
             'Only one variable: $YEAR']
results = []
years = ['2018', 2018]
names = ['Michael Newman', 'Michael']
expected_failures = ['this is an invalidly $ formated template']


class TestParse(unittest.TestCase):

    def test_no_failures(self):
        for test in tests:
            with self.subTest():
                file =self._file_helper(test['template'])

                result = parse_template(file, test['args'])
                self.assertEqual(test['expected'], result)

    def test_failures(self):
        for fail in fails:
            with self.subTest():
                file = self._file_helper(fail['template'])

                with self.assertRaises(fail['type']):
                    parse_template(file, fail['args'])

    def _file_helper(self, template):
        file = tempfile.mkstemp()[1]
        with open(file, 'w+') as f:
            f.write(template)
            f.close()
        return file

