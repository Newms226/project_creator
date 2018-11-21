from src.util.immutable import read_only_properties
import unittest


@read_only_properties('a', 'b')
class Basic:
    def __init__(self):
        self.a = 'A'
        self.b = 'B'
        self.c = 'c'


class TestReadOnly(unittest.TestCase):

    def setUp(self):
        self.basic = Basic()

    def test_read(self):
        self.assertEqual('A', self.basic.a)
        self.assertEqual('B', self.basic.b)

    def test_set(self):
        with self.assertRaises(AttributeError):
            self.basic.a = 'b'
            self.basic.b = 'c'
            self.basic.a.__dict__['a'] = 'b'
            self.basic.a.__setattr__('a', 'b')

        self.basic.c = 'CC'
        self.assertEqual('CC', self.basic.c)

    def test_delete(self):
        with self.assertRaises(AttributeError):
            del self.basic.a
            del self.basic.b

        del self.basic.c
        self.assertFalse(hasattr(self.basic, 'c'))

if __name__ == '__main__':
    unittest.main()