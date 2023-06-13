def aumentar(n, p):
    aum = n + (n * p/100)
    return aum


def diminuir(n, p):
    des = n - (n * p/100)
    return des


def dobro(n):
    dob = n * 2
    return dob


def metade(n):
    met = n/2
    return met


def moeda(n):
    reais = f'R${n}'
    return reais
