numeros = [[], []]
num = 0

for n in range(1, 8):
    num = int(input(f'{n}/7  Digite um valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'\nPares: {numeros[0]}')
print(f'Ímpares: {numeros[1]}')

