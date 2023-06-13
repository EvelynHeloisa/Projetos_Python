print('='*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('='*40)

produtos = ('Caneta', 8.5,
            'Apontador', 2.4,
            'Caderno Grande', 12.60,
            'Lápis de Colorir', 10.0,
            'Régua', 5.3,
            'Mochila Feminina', 78.90,
            'Estojo', 15.90,
            'Pasta Plástica', 3.20,
            'Livros', 98.70,)

for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<32}', end='')
    else:
        print(f'R$ {produtos[p]:>5.2f}')
print('='*40)
