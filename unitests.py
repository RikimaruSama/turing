import unittest
from module import file_to_dict
from mt import Bande, MT


class Testing(unittest.TestCase):

  def test_create_mt(self):
    dico = file_to_dict("binary_palindrome.txt")
    a = MT(dico)
    b = Bande("010")
    a.add(b)
    a.run(10, draw=False)
    self.assertIsInstance(a, MT)

  def test_copy(self):
    dico = file_to_dict("fast_palindrome.txt")
    a = MT(dico)
    b, c = Bande("010"), Bande()
    a.add(b)
    a.add(c)
    a.copy(0, 1)
    self.assertEqual(b.characters, c.characters)

  def test_erase(self):
    dico = file_to_dict("fast_palindrome.txt")
    a = MT(dico)
    b, c = Bande("010"), Bande()
    a.add(b)
    a.add(c)
    a.erase(0)
    self.assertNotIn(b, a.bandes)

  def test_search(self):
    dico = file_to_dict("fast_palindrome.txt")
    a = MT(dico)
    b = Bande('111010')
    a.add(b)
    self.assertEqual(a.search(0,'0',False), 3)
    
  def test_left(self):
    dico = file_to_dict("fast_palindrome.txt")
    a = MT(dico)
    b = Bande('10101')
    a.add(b)
    self.assertEqual(a.left(0), 4)

if __name__ == '__main__':
  unittest.main()
