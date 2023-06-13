cont = soma = num = 0
print('='*40)
while True:
    num = int(input("Digite um número (999 para parar): "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores é {soma}')
