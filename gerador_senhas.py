# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/b2a55174-2b3d-44ac-b148-4e7591415aa4

import random
import string

tamanho = 8  # int(input('Digite o tamanho da senha a ser gerada: '))

chars = string.ascii_letters + string.digits + '!.,-_@#$%&*()+=/'
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
