print('='*40)
print('   TENTE ADVINHAR UM NÚMERO DE 0 A 5')
print('='*40)

import random
sorteado = random.randint(0,5)

numero = int(input('Qual é o número? '))

from time import sleep
print('Processando.', end="")
sleep(1)
print('.', end="")
sleep(1)
print('.')
sleep(1)

if sorteado == numero:
    print('\nVocê acertou! Parabéns!')
else:
    print('\nErrou... Tente novamente.')
