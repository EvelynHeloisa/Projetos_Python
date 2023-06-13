def aumentar(n=0, p=0):
    aum = n + (n * p/100)
    return aum


def diminuir(n=0, p=0):
    des = n - (n * p/100)
    return des


def dobro(n=0):
    dob = n * 2
    return dob


def metade(n=0):
    met = n/2
    return met


def moeda(preço=0, moeda='R$'):
    res = f'{moeda}{preço:.2f}'.replace('.', ',')
    return res


