# Fatorial com comando for

print('='*30)
print('{:^30}'.format('FATORIAL'))
print('='*30)

num = int(input('Digite um número para \ncalcular seu fatorial: '))
fat = 1

for i in range(num, 1, (num-1)):
    fat *= num
print('O fatoral é {}'.format(fat))
