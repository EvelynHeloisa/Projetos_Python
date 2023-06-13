# import random
# num = random.randint(1, 20)
# print(num)

from math import floor
print('VAMOS LER A PARTE INTEIRA DE UM NÙMERO\n')
num = float(input('Digite um número real: '))
piso = floor(num)
print('A parte inteira de {} é {}'.format(num, piso))
