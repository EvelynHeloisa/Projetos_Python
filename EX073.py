print('='*60)
print('{:^60}'.format('BRASILEIRÃO 2022'))
print('='*60)

times20 = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias',
           'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
           'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
            'Bragantino', 'Coritiba', 'Cuiába', 'Ceará SC', 'Atlético-GO',
           'Avaí', 'Juventude')

print('Os 5 Primeiros Colocados foram:\n')
for c in range(0,5):
    print(f'{c+1}° {times20[c]}')
print('='*60)

print('Os ultímos 4 colocados foram:\n')
print(times20[-4:])
print('='*60)

print('Times em ordem Alfabética:\n')
print(sorted(times20))
print('='*60)

pos = times20.index('Avaí')+1
print(f'O time do Avaí está na {pos}° posição')
