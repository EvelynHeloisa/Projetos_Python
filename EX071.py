print('='*40)
print('{:^40}'.format("EVI'S DEV BANK"))
print('='*40)

c_50 = c_20 = c_10 = c_1 = 0

valor = int(input('Qual valor você quer sacar? '))
cont_valor = valor

while True:
    if cont_valor >= 50:
        cont_valor -= 50
        c_50 += 1
    else:
        break
while True:
    if cont_valor >= 20:
        cont_valor -= 20
        c_20 += 1
    else:
        break
while True:
    if cont_valor >= 10:
        cont_valor -= 10
        c_10 += 1
    else:
        break
while True:
    if cont_valor >= 1:
        cont_valor -= 1
        c_1 += 1
    else:
        break


print('='*40)
print(f'Notas de R$50: {c_50}')
print(f'Notas de R$20: {c_20}')
print(f'Notas de R$10: {c_10}')
print(f'Notas de R$01: {c_1}')



