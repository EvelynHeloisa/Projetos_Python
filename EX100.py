from random import randint
from time import sleep
números = list()


def sortear(números):
    print(f'Sorteando 5 números aleatórios...')
    for i in range(0, 5):
        i = randint(1, 10)
        números.append(i)
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)


def somarPar(números):
    soma = 0
    for i in números:
        if i % 2 == 0:
            soma += i
    print(f'\nA soma de todos os números pares é {soma}')


sortear(números)
somarPar(números)
