numeros = list()
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))

for cont, n in enumerate(numeros):
    print(f'Posição {cont+1}: Número: {n}!!')
print('FIM...')
