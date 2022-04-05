# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/99c7ffdd-2126-4454-9d75-12b9d0203db0
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket Criado com Sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\nServidor: Oláaaaa Cliente'
while True:
    dados, end = s.recvfrom(4096)
    if dados:
        print('servidor enviando mensagem')
        s.sendto(dados + (mensagem.encode()), end)
