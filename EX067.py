print('='*40)
print('{:^40}'.format('TABUADA'))
print('='*40)

print('Para encerrar o programa \ndigite um número negaivo ou 0')

num = 0
cont = 1
soma = 0
mult = True

while True:
    print('='*40)
    num = int(input('Quer ver a tabuada de qual número: '))
    if num <= 0:
        break
    for cont in range(1, 11):
         soma = num * cont
         print(f'{num} X {cont} = {soma}')

print('='*40)
print('\nPrograma encerrado.')