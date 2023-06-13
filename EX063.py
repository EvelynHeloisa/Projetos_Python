print('='*40)
print('{:^40}'.format('SEQUÊNCIA DE FIBONACCI'))
print('='*40)

n = int(input("Digite quantos números deseja ver: "))
f1 = 0
f2 = 1
cont = 3

print('{} {}'.format(f1, f2), end=' ')

while cont <= n:
    f3 = f1 + f2
    print(f3, end=' ')
    f1 = f2
    f2 = f3
    cont += 1
