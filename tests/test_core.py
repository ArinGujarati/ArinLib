import unittest
from ArinLib import ObjectToInt

class TestCore(unittest.TestCase):
    def test(self):
        ObjectToInt(['A','B','C'])

if __name__ == '__main__':
    unittest.main()
