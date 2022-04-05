# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/1a0f9a2a-47cb-4b92-9013-1cb8d077b147
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket Criado com Sucesso!!!')

host = 'localhost'
porta = 5432
mensagem = 'Olá servidor. firmeza?'

try:
    s.sendto(mensagem.encode(), (host, porta))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
