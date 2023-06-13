from random import randint
from time import sleep
from operator import itemgetter

jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}

ranking = list()

for k, v in jogos.items():
    print(f'O {k} jogou {v}')
    sleep(0.8)
print('-'*30)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} | Dado: {v[1]}')
    sleep(0.8)
