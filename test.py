import unittest, csv, os
# THIS_DIR = os.path.dirname(os.path.abspath(__file__))
from csv_parser import test


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        #parser.
        #self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(test(), 1)
        #self.assertCo


if __name__ == '__main__':
    unittest.main()