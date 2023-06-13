def aumentar(n=0, p=0, formatado=False):
    aum = n + (n * p/100)
    return aum if formatado is False else moeda(aum)


def diminuir(n=0, p=0, formatado=False):
    des = n - (n * p/100)
    return des if formatado is False else moeda(des)


def dobro(n=0, formatado=False):
    dob = n * 2
    return dob if not formatado else moeda(dob)


def metade(n=0, formatado=False):
    met = n/2
    return met if not formatado else moeda(met)


def moeda(preco=0, moeda='R$'):
    res = f'{moeda}{preco:.2f}'.replace('.', ',')
    return res


def resumo(preco=0, por_aum=10, por_red=15):
    print('='*30)
    print('ANALIZANDO OS VALORES'.center(30))
    print('='*30)

    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'{por_red}% de Desconto: \t{diminuir(preco,por_red, True)}')
    print(f'{por_aum}% de Aumento: \t{aumentar(preco,por_aum, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
