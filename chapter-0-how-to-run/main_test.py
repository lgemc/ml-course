import unittest
from main import sum

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
