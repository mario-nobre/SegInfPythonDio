# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/daf1d8ac-bfcd-48a0-bad8-e277a9642c44

import itertools

texto = input('Digite a palavra a ser permutada: ')

resultado = itertools.permutations(texto, len(texto))

for i in resultado:
    print(''.join(i))
