path = "turing_file.txt"
turing_dict = {'name': None, 'init': None, 'accept': None, 'transitions': []}
alphabet = ['0', '1', '#']


def is_valide(line):
  # si nous avons '' a la place de l'etat ou de la destination etc on quitte
  for data in line.split(','):
    if data == '':
      return False
  if line == '':
    return False
  if line.count(',') == 0:
    return False
    
  chars = len(line.split(','))
  nbr_bandes = (chars - 5) / 3 + 1

  # if on a sur la ligne une difference entre le nombre d'informations
  # si on doit avoir 3 bandes et que l'on n'a pas 11 informations on quitte
  if nbr_bandes % 1 != 0:
    return False
    
  indice_triplet = 2 * nbr_bandes + nbr_bandes - 1
  list_indices = []
  
  while indice_triplet >= 2:
    list_indices.append(indice_triplet)
    indice_triplet = indice_triplet - 3
    
  print('Les indices des transitions sont ' + str(list_indices))
  print('La ligne ci-dessous possede ' + str(nbr_bandes) + ' bande(s)')
  return nbr_bandes, list_indices


# nbr_bandes = (11 - 5) / 3 + 1
# nombre de bandes = ( nombre de caractere - 5 % 3 ) == 0 valide => /3 + 1 = nombre de bandes
# index du nombre de bande = 2 * (nbr de bandes total k) + k-1

with open(path, "r") as f:
  line = f.readline().replace("\n", "")
  turing_dict['name'] = line.split(":")[1].replace(" ", "", 1)

  line = f.readline().replace("\n", "")
  turing_dict['init'] = line.split(":")[1].replace(" ", "", 1)

  line = f.readline().replace("\n", "")
  turing_dict['accept'] = line.split(":")[1].replace(" ", "", 1)

  for line in f.readlines():
    line = line.replace("\n", "")
    if is_valide(line):
      transition = line.split(',')
      print(line)
print(turing_dict)
