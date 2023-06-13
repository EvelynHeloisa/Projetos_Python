print('='*40)
print('\n          RADAR DE VELOCIDADE\n')
print('='*40)
print('  Multa de R$ 7 por cada km excedido.')
print('='*40)

vel = float(input('Digite a velocidade do carro em KM: '))
multa = (vel - 80) * 7

if vel > 80:
    print('\nA velocidade máxima permitida (80km/h) foi excedida.')
    print('Sua multa será de R$ {}'.format(multa))
else:
    print('\nVelocidade dentro da permitida!')