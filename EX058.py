print('='*40)
print('{:^40}'.format('JOGO DA ADVINHAÇÃO'))
print('='*40)

from random import randint

comp = randint(1, 10)
jogad = int(input('Escolha um número entre 1 e 10: '))
tent = 0

while comp != jogad:
    if jogad < comp:
        jogad = int(input('Quase lá... Um pouco mais...\n Tente novamente: '))
        tent += 1
    elif jogad > comp:
        jogad = int(input('Um pouco menos... Vamos lá.. \n Tente novamente: '))
        tent += 1
print('='*40)
print('Acertou! O número foi {}\n Tentativas: {}'.format(comp, tent))