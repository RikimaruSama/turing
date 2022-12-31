import unittest
from module import file_to_dict
from mt import Bande, MT

class Testing(unittest.TestCase):
  
    def test_create_mt(self):
      dico = file_to_dict("binary_palindrome.txt")
      a = MT(dico)
      b = Bande("010")
      a.add(b)
      a.run(10)
      self.assertIsInstance(a, MT)

    def test_copy(self):
      dico = file_to_dict("fast_palindrome.txt")
      a = MT(dico)
      b, c = Bande("010"), Bande()
      a.add(b)
      a.add(c)
      from copy import copy
      a.copy(b, c)
      self.assertEqual(a, b)
    def test_erase(self):
      pass
    def test_search(self):
      pass
    def test_left(self):
      pass

if __name__ == '__main__':
    unittest.main()
