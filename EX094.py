pessoa = {}
lista = list()
media = 0
mulheres = []
acima_media = []

while True:
    pessoa['Nome'] = str(input('Nome do usúario: ')).strip().title()
    while True:
        pessoa['Sexo'] = str(input('Sexo [F/M]: ')).upper().strip()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('ERRO! Digite apenas [M] ou [F]')

    pessoa['Idade'] = int(input('Idade: '))
    media += pessoa['Idade']
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa.copy())
    lista.append(pessoa.copy())

    while True:
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opc in 'SN':
            break
        print('ERRO! Digite apenas [S] ou [N]')
    if opc == 'N':
        break

print('='*40)
print(f'Total de pessoas cadastradas: {len(lista)}')
media = media / len(lista)
print(f'Média de idade: {media:.0f}')

print('-'*40)
print(f'{"Lista das Mulheres:":^40}')
for m in mulheres:
    for k, v in m.items():
        print(f'{k:>3}:{v:>5}', end=' | ')
    print('')

print('-'*40)
for l in lista:
    if l['Idade'] >= media:
        acima_media.append(l)
print(f'{"Pessoas com a idade acima da média:":^40}')
for a in acima_media:
    for k, v in a.items():
        print(f'{k:>3}: {v:>5}', end=' | ')
    print('')

