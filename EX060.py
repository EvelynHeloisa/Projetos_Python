print('='*30)
print('{:^30}'.format('FATORIAL'))
print('='*30)

num = int(input('Digite um número para \ncalcular seu fatorial: '))
fat = 1

while num >= 1:
    print('{}'.format(num), 'x ' if num > 1 else ' = ' '{}'.format(fat), end='')
    fat = fat * num
    num -= 1

print('\n\nFatorial = {}'.format(fat))
