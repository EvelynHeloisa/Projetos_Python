jogador = {}
partidas = list()
tot = 0

jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['N° Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range(0, jogador['N° Partidas']):
    partidas.append(int(input(f'    Quantos gols na partida {p+1}? ')))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('='*40)

for k, v in jogador.items():
    print(f'{k}: {v}')

print('='*40)

print(f'Jogador {jogador["Nome"]} jogou {jogador["N° Partidas"]} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'    Na partida {i} fez {v} gols.')
print(f'Total de gols {jogador["Total"]}')

