import ctypes

atributo_ocultar = 0x01  # para ocultar coloque '0x02'

caminho = 'ocultar.txt'

retorno = ctypes.windll.kernel32.SetFileAttributesW(caminho, atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else:
    print('Arquivo não ocultado')
