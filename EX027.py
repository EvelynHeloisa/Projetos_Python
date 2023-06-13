print('='*40)
print('   CALCULANDO O PREÇO DA PASSAGEM')
print('='*40)

distancia = float(input('Insira a distância da viagem em km: '))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print('O preço da passagem será de R$ {:.2f}'.format(preço))

# FORMA SIMPLIFICADA
# preço = distancia * 0.5 if distancia <= 200 else distancia = 0.45