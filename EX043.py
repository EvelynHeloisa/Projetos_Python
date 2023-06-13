print('\033[35m=\033[m'*60)
print('         CALCÚLO DE IMC (ÍNDICE DE MASSA CORPORAL)')
print('\033[35m=\033[m'*60)

peso = float(input('          |     Informe seu peso (kg): '))
altura = float(input('          |     Iforme sua altura (m): '))
imc = peso / (altura**2)
print('\033[35m      ===============================================\033[m')
print('          |     IMC: {:.1f}'.format(imc))

if imc < 18.5:
    print('          |     Você está abaixo do peso.')
elif imc < 25:
    print('          |     Você está no peso ideal.')
elif imc < 30:
    print('          |     Você está com sobrepeso.')
elif imc < 40:
    print('          |     Você está em obesidade.')
elif imc >= 40:
    print('          |     Você está em obesidade morbida.')
