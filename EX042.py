print('='*40)
print('         FORMANDO UM TRIÂNGULO')
print('='*40)

a = float(input('Insira o tamanho da primeira reta: '))
b = float(input('Insira o tamanho da segunda reta: '))
c = float(input('Insira o tamanho da terceira reta: '))
print('='*40)
# a soma de dois lados é sempre menor que o terceiro lado.

if a < b+c and b < a+c and c < a+b:
    print('As três retas acima PODEM formar um TRIÂNGULO ', end='')
    if a!= b != c != a:
        print('ESCALENO')
    elif a == b == c:
        print('EQUILÁTERO')
    else:
        print('ISÓCELES')
else:
    print('Os três segmentos de reta acima NÃO podem formar um TRIÂNGULO')