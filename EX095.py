jogador = {}
partidas = list()
tot = 0
time = list()

while True:
    print('='*40)
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['N° Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for p in range(0, jogador['N° Partidas']):
        partidas.append(int(input(f'    Quantos gols na partida {p+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    print('='*40)

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Cadastrar outro jogador? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break

print('='*40)
print(f'{"RELATÓRIO DO TIME":^40}')
print('Cód ', end='  ')
for i in jogador.keys():
    print(f'{i:<14}', end='')
print()

for k, v in enumerate(time):
    print(f'{k}', end='   ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    print('='*40)
    cod = int(input('Deseja ver dados de qual jogador? \n(999 para parar) '))
    print('-'*40)
    if cod == 999:
        break
    elif cod >= len(time):
        print(f'ERRO! Não existe jogador com o código {cod}')
    else:
        print(f'Jogador {time[cod]["Nome"]}')
        for i, g in enumerate(time[cod]["Gols"]):
            print(f'Na parida {i+1} fez {g} gols.')

print('FIM DO PROGRAMA...')
