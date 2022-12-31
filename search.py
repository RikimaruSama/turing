def search(self, i, a):
  index_tete = 0
  for char in self.bandes[i].characters:
    if char != '_' and char == a:
      print("SEARCH(bande " + str(i) + "): " + char + " pour l'index " + str(index_tete))
      return index_tete
    index_tete += 1