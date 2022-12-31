class MT:

  def __init__(self,dico=None,
               etat_actuel=None,
               etat_final=None,
               transitions=None,
               alphabet=None,
               bandes=[],
               refs=[]):
    if dico == None:
      self.etat_actuel,self.etat_final,self.transitions,self.alphabet = etat_actuel, etat_final, transitions, alphabet
      self.bandes, self.refs = bandes, refs
    else:
      self.etat_actuel = dico['init']
      self.etat_final = dico['accept']
      self.transitions = dico["transitions"]
      self.alphabet = dico["alphabet"]
      self.bandes = []
      self.refs = dico['refs']
                 
  def setter_etat(self, etat):
    self.etat_actuel = etat

  def add(self,bande):
    self.bandes.append(bande)
  
  def run(self, max_iter=100):
    iter = 0
    print("------------------- initialisation")
    for bande in self.bandes:
      print(bande)
    while self.etat_actuel != self.etat_final and iter < max_iter:
      self.step()
      print("------------------- etape: " + str(iter))
      for bande in self.bandes:
        print(bande)
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
        if check == check_t:
          for buff in zip(self.bandes, self.refs):
            buff[0].write_tete(transition[buff[1] + 1])
            buff[0].move_tete(transition[buff[1] + 2])
          self.setter_etat(transition[1])
          break
        check.clear()
        check_t.clear()
  
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

  def __str__(self):
    value, buff = "|", ""
    for char in self.characters:
      value += char
    buff = (self.index_tete+1) * " "
    value += "|\n" + buff + "^"
    return value