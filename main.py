class MT:

  def __init__(self, etats=None, transitions=None, alphabet=None):
    self.etats = etats
    self.transitions = transitions
    self.alphabet = alphabet

class Bande:

  def __init__(self, characters='#', tete_de_lect=None, alphabets=None):
    self.characters = list(characters)
    self.alphabets = alphabets
    for letter in list(characters):
      if letter not in alphabets:
        raise TypeError('La bande est composée de characteres non valide.')
      self.tete_de_lect = characters[0]

  def move_tete(self, symbole):
    pass

  def __print__(self):
    pass


a = MT()
alphabets = ('1', '0', '#')
mot = '100'
b = Bande(mot, tete_de_lect = mot[:1],alphabets=alphabets)
etats = ('Q1', 'Q2', 'Qfinal')
transitions = {}
for etat in etats:
  for letter in alphabets:
    transitions.update({etat: {0: None, 1: None, '#': None}})
