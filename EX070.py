print('='*40)
print('{:^40}'.format("EVI'S MAGAZINE"))

tot = pro_mil = pre_m_bar = cont = 0
pro_m_bar = ' '

while True:

    print('='*40)
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço R$: '))
    tot += preco
    cont += 1

    if preco > 1000:
        pro_mil += 1

    if cont == 1 or preco < pre_m_bar:
        pre_m_bar = preco
        pro_m_bar = produto

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if opcao == 'N':
         break

print('='*40)
print(f'\nTotal da Compra R$: {tot}')
print(f'Produtos custando mais que R$ 1.000: {pro_mil}')
print(f'Produto mais barato: {pro_m_bar} | Preço R$ {pre_m_bar}')



