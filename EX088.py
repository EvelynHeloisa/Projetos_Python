from random import randint
from time import sleep

print('='*40)
print('{:^40}'.format('JOGANDO NA MEGA SENA'))
print('='*40)

jog = int(input('Quantos jogos quer sortear? '))
lista = []
jogos = []
cont = tot = 0

for i in range(0, jog):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print('='*40)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)


