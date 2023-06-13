numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
        'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = 0
    num = int(input('Digite um número de 0 a 20: '))

    while num < 0 or num > 20:
        num = int(input('Tente novamente! Digite um número de 0 a 20: '))

    print(f'Número por extenso: {numeros[num]}')
    print('='*40)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
