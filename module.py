def file_to_dict(path):
  turing_dict = {
    'name': None,
    'init': None,
    'accept': None,
    'alphabet': ('0', '1', '_'),
    'transitions': [],
    'refs': []
  }
  with open(path, "r") as f:
    line = f.readline().replace("\n", "")
    turing_dict['name'] = line.replace(" ", "", 1)

    line = f.readline().replace("\n", "")
    turing_dict['init'] = line.replace(" ", "", 1)

    line = f.readline().replace("\n", "")
    turing_dict['accept'] = line.replace(" ", "", 1).split(',')

    line = f.readline().replace("\n", "")
    checkERR(line, turing_dict["alphabet"])
    turing_dict["refs"] = info_bande(line)
    turing_dict["transitions"].append(line.split(','))
    for line in f.readlines():
      line = line.replace("\n", "")
      checkERR(line,turing_dict["alphabet"])
      turing_dict["transitions"].append(line.split(','))
  return turing_dict

def checkERR(line,alphabet):
  if not isinstance(line,str):
    raise TypeError("Compréhention non adapté, une ligne n'est pas une chaine de characteres.")
  if line == '': raise SyntaxError("Compréhention non adapté, une ligne est vide.")
    
  nbr_bandes = (len(line.split(',')) - 5) / 3 + 1
  indice_triplet = 2 * int(nbr_bandes) + int(nbr_bandes) - 1
  parts = line.split(',')
  for i in range(len(parts)-1):
    if parts[i] == '':
      raise SyntaxError("Argument(s) manquant(s)/vide(s): " + parts[i]) 
    if parts[indice_triplet] not in alphabet:
      raise SyntaxError("Argument(s) invalide, lecture non valide " + line + '.')
      indice_triplet += 1
    if parts[indice_triplet+1] not in alphabet:
      raise SyntaxError("Argument(s) invalide, ecriture non valide " + line + '.')
      indice_triplet += 1
    if parts[indice_triplet+2] not in ('-','<','>'):
      raise SyntaxError("Argument(s) invalide, deplacement non valide " + line + '.')
      indice_triplet += 1
    
  if nbr_bandes % 1 != 0:
    raise SyntaxError("Argument(s) necessaire(s) pour la ligne " + line + ".")

def info_bande(line):
  nbr_bandes = int((len(line.split(',')) - 5) / 3 + 1)
  return [ref for ref in range(2, 2 * nbr_bandes + nbr_bandes, 3)]
