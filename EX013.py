print('='*60)
print('      Calculando a hipotenusa de um triângulo retângulo')
print('='*60)

from math import sqrt
c1 = int(input('\nInsira o cateto oposto: '))
c2 = int(input('Insira o cateto adjacente: '))
h = sqrt(c1**2 + c2**2)
print('A hipotenusa do trinângulo é', h)
