numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('='*40)
print(f'Lista completa: {numeros}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')