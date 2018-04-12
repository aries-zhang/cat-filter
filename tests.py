import unittest

import unittest

class TempTestMethods(unittest.TestCase):

    def test_number_one(self):
        self.assertEqual('hello'.upper(), 'HELLO')

if __name__ == '__main__':
    unittest.main()