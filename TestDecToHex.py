import unittest
from dec_to_hex import dec_to_hex


class TestDecToHex(unittest.TestCase):

    def test_dec_to_hex(self):
        self.assertEqual(dec_to_hex(10), 'A')
        self.assertEqual(dec_to_hex(16), '10')
        self.assertEqual(dec_to_hex(255), 'FF')


if __name__ == '__main__':
    unittest.main()