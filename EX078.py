num = []

for n in range(0, 5):
    num.append(int(input(f' {n+1}/5 Digite um número: ')))


print(f'Maior valor: {max(num)}   | Posições: ', end='')
for pos, n in enumerate(num):
    if n == max(num):
        print(f'{pos} - ', end='')

print(f'\nMenor valor: {min(num)} | Posições: ', end='')
for pos, n in enumerate(num):
    if n == min(num):
        print(f'{pos} - ', end='')
