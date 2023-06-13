print('='*40)
print('{:^40}'.format('TABUADA'))
print('='*40)

num = int(input('Digite um número para ver a tabuada: '))
res = 0

for c in range(1, 11):
    res = num * c
    print('              {} X {} = {}'.format(num, c, res))
print('='*40)