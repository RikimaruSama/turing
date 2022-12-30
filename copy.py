def left():
  from file_module import file_to_dict
  dicto = file_to_dict("turing_file.txt")
  a = Bande(characters='10100')
  b = MT(etat_actuel=dicto['init'],
         etat_final=dicto['accept'],
         alphabet=dicto["alphabet"],
         transitions=dicto["transitions"],
         bandes=[a],
         refs=dicto["refs"])