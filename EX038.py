n1 = int(input('insira o primeiro valor: '))
n2 = int(input('Insira o o segundo valor: '))

if n1 > n2:
    print('{} é maior do que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior do que {}'.format(n2, n1))
else:
    print('Os dois valores são iguais.')
