import unittest, csv, os
# THIS_DIR = os.path.dirname(os.path.abspath(__file__))
import csv_parser


class TestScript(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len(csv_parser.main()), 12)


if __name__ == '__main__':
    unittest.main()