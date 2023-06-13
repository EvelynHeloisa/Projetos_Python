print(' O número é par ou ímpar?\n')

numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0: # O resto da divisão de qualquer número par é 0
    print('{} é PAR'.format(numero))
else:
    print('{} é ÍMPAR'.format(numero))