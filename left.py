def left(self, i):
  for char in self.bandes[i].characters[::-1]:
    if char != '_':
      print("LEFT(bande " + str(i) + "): " + char)
      return char