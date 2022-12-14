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
      self.etat_actuel = 'q0'
    self.etat_final = etat_final
    self.transitions = transitions
    self.alphabet = alphabet
    self.bandes = bandes
    self.refs = refs

  def setter_etat(self, etat):
    self.etat_actuel = etat

  # On regarde toutes les transitions, toutes les bandes et toutes les refs
  def etape(self):
    for i, bande in enumerate(self.bandes):
      for transition in self.transitions:
        if transition[0] == self.etat_actuel and bande.characters[
            bande.index_tete] == transition[self.refs[i]]:
          print('Changement !')
          bande.write_tete(transition[self.refs[i] + 1])
          bande.move_tete(transition[self.refs[i] + 2])
          self.setter_etat(transition[1])
          return self.etat_actuel


class Bande:

  def __init__(self,
               characters='#',
               index_tete=0,
               alphabet=('0', '1', '#', '_')):
    self.alphabet = alphabet
    for letter in list(characters):
      if letter not in alphabet:
        raise TypeError('La bande est composée de characteres non valide.')
    self.characters = list(characters)
    self.index_tete = index_tete

  def move_tete(self, symbole):
    moves = {'-': 0, '>': 1, '<': -1}
    self.index_tete = self.index_tete + moves.get(symbole)

  def write_tete(self, new_char):
    if new_char == '_':
      self.characters[self.index_tete] = '_'
    else:
      if self.index_tete == len(self.characters) - 1:
        self.characters.append('_')
      elif self.index_tete == -1:
        self.characters.insert(0, '_')
        self.characters[self.index_tete] = new_char
      else:
        self.characters[self.index_tete] = new_char
      return


def main():
  from file_module import file_to_dict
  dicto = file_to_dict("turing_file.txt")
  a = Bande(characters='10100')
  b = MT(etat_actuel=dicto['init'],
         etat_final=dicto['accept'],
         alphabet=dicto["alphabet"],
         transitions=dicto["transitions"],
         bandes=[a],
         refs=dicto["ref"])
  print(b.transitions)
  print("\n")
  for i, bande in enumerate(b.bandes):
    for transition in b.transitions:
      print(i, bande, bande.characters)
      print("\n")
      print(transition[0], b.etat_actuel, bande.characters[bande.index_tete],
            transition[b.refs[i]])
    print("\n")

  print("\n")
  print(a.characters)
  while b.etat_actuel != b.etat_final:
    b.etape()
    print(a.characters)
  print("Accept !")


main()
