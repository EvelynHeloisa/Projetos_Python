print('SOMANDO...')
soma = 0
cont = 0
for c in range(0,6):
    num = int(input('{}/6    Digite um valor: '.format(c+1)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\nTotal de números pares = {} \nSoma = {}'.format(cont, soma))