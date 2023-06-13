resp = 'S'
soma = cont = med = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print('-'*30)
med = soma / cont
print('A média dos números digitados é {:.2f}'.format(med))
print('Maior número: {} \nMenor número: {}'.format(maior, menor))