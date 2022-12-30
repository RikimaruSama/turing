class MT:

  def __init__(self,
               etat_actuel=None,
               etat_final=None,
               transitions=None,
               alphabet=None,
               bandes=[],
               refs=[]):
    self.etat_actuel = etat_actuel
    if self.etat_actuel == None:
      self.etat_actuel = etat_actuel
    self.etat_final = etat_final
    self.transitions = transitions
    self.alphabet = alphabet
    self.bandes = bandes
    self.refs = refs

  def setter_etat(self, etat):
    self.etat_actuel = etat

  def run(self, max_iter=100):
    iter = 0
    for bande in self.bandes:
      print(bande.characters, bande.index_tete)
    while self.etat_actuel != self.etat_final and iter < max_iter:
      self.step()
      print("\n")
      for bande in self.bandes:
        print(bande.characters, bande.index_tete)
      iter += 1
      if iter == max_iter:
        print("rejeted")
        return False
    print("accepted")
    return True

  def step(self):
    check, check_t = list(), list()
    for transition in self.transitions:
      if transition[0] == self.etat_actuel:
        for bande in self.bandes:
          check.append(bande.characters[bande.index_tete])
        for ref in self.refs:
          check_t.append(transition[ref])
        print("On regarde si: " + self.etat_actuel + " " + str(check) + " = " +
              str(check_t))
        if check == check_t:
          for buff in zip(self.bandes, self.refs):
            buff[0].write_tete(transition[buff[1] + 1])
            buff[0].move_tete(transition[buff[1] + 2])
          self.setter_etat(transition[1])
          break
        check.clear()
        check_t.clear()

  def left(self, i):
    for char in self.bandes[i].characters[::-1]:
      if char != '_':
        print("LEFT(bande " + str(i) + "): " + char)
        return char

  def erase(self, i):
    del self.bandes[i]

  def search(self, i, a):
    index_tete = 0
    for char in self.bandes[i].characters:
      if char != '_' and char == a:
        print("SEARCH(bande " + str(i) + "): " + char + " pour l'index " +
              str(index_tete))
        return index_tete
      index_tete += 1

  def copy(self, i, j):
    self.bandes[j].characters = self.bandes[i].characters.copy()
    self.bandes[j].index_tete = self.bandes[i].index_tete
    self.bandes[j].alphabet = self.bandes[i].alphabet

  def __str__(self):
    


class Bande:

  def __init__(self, characters='_', index_tete=0, alphabet=('0', '1', '_')):
    self.alphabet = alphabet
    for letter in list(characters):
      if letter not in alphabet:
        raise TypeError('La bande est composée de characteres non valide.')
    self.characters = list(characters)
    self.index_tete = index_tete

  def move_tete(self, symbole):
    moves = {'-': 0, '>': 1, '<': -1}
    self.index_tete += moves.get(symbole)
    if self.index_tete == -1:
      self.characters.insert(0, '_')
      self.index_tete = 0

  def write_tete(self, new_char):
    if self.index_tete == len(self.characters) - 1:
      self.characters.append('_')
    self.characters[self.index_tete] = new_char


def main():
  from file_module import file_to_dict
  dicto = file_to_dict("turing_file.txt")
  a = Bande(characters='10100')
  b = MT(etat_actuel=dicto['init'],
         etat_final=dicto['accept'],
         alphabet=dicto["alphabet"],
         transitions=dicto["transitions"],
         bandes=[a],
         refs=dicto["refs"])

  b.run(100)


def main2():
  print("Debut de programme...\n")
  from file_module import file_to_dict
  dicto = file_to_dict("fast_palindrome.txt")
  b1 = Bande(characters='10')
  b2 = Bande()
  b = MT(etat_actuel=dicto['init'],
         etat_final=dicto['accept'],
         alphabet=dicto["alphabet"],
         transitions=dicto["transitions"],
         bandes=[b1, b2],
         refs=dicto["refs"])
  b.run(10)
  #LEFT
  b.left(0)
  #ERASE
  #SEARCH
  b.search(0, '1')
  #COPY
  b.copy(0, 1)

  print("...Fin de programme")

main2()

import unittest

class Testing(unittest.TestCase):
  
    def create_mt(self):
        self.assertTrue(True)

#if __name__ == '__main__':
#    unittest.main()
