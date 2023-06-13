print('SOMA DE TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE 3 NO INTERVALO DE 1 ATÉ 500')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('RESULTADO:', soma)
print('TOTAL DE NÚMEROS:', cont)
