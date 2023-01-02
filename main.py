from module import file_to_dict
from mt import Bande, MT

dico = file_to_dict("binary_palindrome.txt")
a = MT(dico)
b = Bande("0100")
a.add(b)
a.run(draw=True)
