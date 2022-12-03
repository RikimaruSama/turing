class MT:

  def __init__(self, etats=None, transitions=None, alphabet=None):
    self.etats = etats
    self.transitions = transitions
    self.alphabet = alphabet

class Bande:

  def __init__(self, characters='#', tete_de_lect=None, alphabet=None):
    self.alphabet = alphabet
    for letter in list(characters):
      if letter not in alphabets:
        raise TypeError('La bande est composée de characteres non valide.')
      self.characters = list(characters)
      self.tete_de_lect = characters[0]

  def move_tete(self, symbole):
    pass

  def __print__(self):
    pass


a = MT()
b = Bande('1001')
etats = ('Q1', 'Q2', 'Qfinal')
alphabets = ('1', '2', '#')
transitions = {}
for etat in etats:
  for letter in alphabets:
    transitions.update({etat: {1: None, 2: None, '#': None}})
