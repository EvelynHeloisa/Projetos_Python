print('='*30)
print('{:^30}'.format('PROGRESSÃO ARITIMÉTICA'))
print('='*30)

a1 = int(input('Primeiro termo da PA: '))
raz = int(input("Digite a razão da PA: "))
an = a1 + (11 - 1) * raz

print('\nOs 10 primeiros termos dessa PA são:')

for pa in range(a1, an, raz):
    print(pa)
