print('='*40)
print('{:^40}'.format('MOSTRANDO O MAIOR E MENOR PESO'))
print('='*40)

peso = {}
tem = 0

for pessoa in range(1, 6):
    peso[pessoa] = float(input('Digite o peso da {}° pessoa: '.format(pessoa)))

for c in range(1, 6):
    for i in range(1, 6):
        if peso[c] < peso[i]:
            tem = peso[c]
            peso[c] = peso[i]
            peso[i] = tem

print('='*40)
print('O menor peso é {}kg'.format(peso[1]))
print('O maior peso é {}kg'.format(peso[5]))
