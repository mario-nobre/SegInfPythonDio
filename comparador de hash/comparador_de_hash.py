# https://web.dio.me/course/seguranca-da-informacao-com-python/learning/0142dcf8-6c08-483f-916d-299512a49b84
import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.hexdigest() != hash2.hexdigest():  # ou - if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print(f'hash1: {hash1.hexdigest()}')
    print(f'hash2: {hash2.hexdigest()}')
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print(f'hash1: {hash1.hexdigest()}')
    print(f'hash2: {hash2.hexdigest()}')
a = 4
