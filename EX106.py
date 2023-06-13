c = ('\033[m', # 0 = sem cores
       '\033[31m', # 1 = vermelho
       '\033[32m', # 2 = verde
       '\033[33m', # 3 = amarelo
       '\033[34m', # 4 = azul
       '\033[35m', # 5 = lilás
       '\033[36m', # 6 = ciano
       '\033[37m', # 7 = cinza
       '\033[38m') # 8 = branco


def ajuda(com):
    help(com)


def tit(msg, cor=4):
    tam = len(msg)
    print(c[cor], end='')
    print('='*tam)
    print(msg)
    print('='*tam)
    print(c[0], end='')



tit('  INTERACTIVE HELP PYTHON  ')

comando = ' '
while True:
    comando = str(input('Qual comando desaja pesquisar? '))

    if comando.upper() == 'FIM':
        break

    else:
        ajuda(comando)
tit(' ATÉ LOGO ', 5)
