def file_to_dict(path):
  turing_dict = {
    'name': None,
    'init': None,
    'accept': None,
    'alphabet': ('0', '1', '#'),
    'nombre_de_bandes': None,
    'transitions': [],
    'ref': []
  }
  with open(path, "r") as f:
    line = f.readline().replace("\n", "")
    turing_dict['name'] = line.replace(" ", "", 1)

    line = f.readline().replace("\n", "")
    turing_dict['init'] = line.replace(" ", "", 1)

    line = f.readline().replace("\n", "")
    turing_dict['accept'] = line.replace(" ", "", 1)

    line = f.readline().replace("\n", "")
    turing_dict['nombre_de_bandes'] = line.replace(" ", "", 1)

    for line in f.readlines():
      line = line.replace("\n", "")
      if is_valide(line):
        if str(int((len(line.split(',')) - 5) / 3 + 1)) != turing_dict['nombre_de_bandes']:
          raise SyntaxError('Nombre de bande insuffisant ou manquant.')
        else:
          turing_dict["ref"] = info_bande(line)
        turing_dict["transitions"].append(line.split(','))
  return turing_dict


def is_valide(line):
  if line == '':
    raise SyntaxError("Format de ligne non adapté: " + line)
  if line.count(',') == 0:
    raise SyntaxError("Compréhention non adapté: " + line)
  for part in line.split(','):
    if part == '':
      raise SyntaxError("Argument(s) manquant(s): " + line)

  nbr_bandes = (len(line.split(',')) - 5) / 3 + 1
  if nbr_bandes % 1 != 0:
    raise SyntaxError("Arguments manquant pour la ligne (" + line + ")")
  return True

def info_bande(line):
  nbr_bandes = (len(line.split(',')) - 5) / 3 + 1
  indice_triplet = 2 * nbr_bandes + nbr_bandes - 1
  list_indices = []
  while indice_triplet >= 2:
    list_indices.append(int(indice_triplet))
    indice_triplet = indice_triplet - 3
  return list_indices
