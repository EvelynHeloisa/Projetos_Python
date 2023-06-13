def ficha(jog, gols=0):
    if jog.strip() == '':
        jog = str('desconhecido')
    print(f'Jogador [{jog}] fez {gols} gols no campionato.')


print('-'*30)
nome = str(input('Nome do jogador: ')).title().strip()
tot = str(input('Total de gols: '))
if tot.isnumeric():
    tot = int(tot)
else:
    tot = 0

ficha(nome, tot)
