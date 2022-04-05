# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/28322528-2783-40c5-b137-870fe8e96392

from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto < 30:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto {piloto} Km: {trajeto}\n')


t_carro1 = Thread(target=carro, args=[1, 'Mario'])
t_carro2 = Thread(target=carro, args=[5, 'Rian'])

t_carro1.start()
t_carro2.start()
