pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).upper())
    dados.append(float(input('Peso em kg: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

print('='*40)
print(f'Total de pessoas cadastradas: {len(pessoas)}')

print(f'Pessoas mais leves: {menor}kg', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nPessoas mais pesadas: {maior}', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
