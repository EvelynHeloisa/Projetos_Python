cont = 1
while True:
    print(cont, end=' ')
    cont += 1
    if cont == 16:
        break

n = soma = 0


print("="*40)

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
print(f'A soma é {soma}')

salario = 93.5623

print(f'O slaário é R${salario:.2f}')
