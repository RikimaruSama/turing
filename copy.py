from mt import Bande, MT

def copy(self, i, j):
  self.bandes[j].characters = self.bandes[i].characters.copy()
  self.bandes[j].index_tete = self.bandes[i].index_tete
  self.bandes[j].alphabet = self.bandes[i].alphabet