print('='*50)
print('{:^40}'.format('PALÍNDROMOS'))
print('='*50)

texto = str(input('Digite uma frase ou palavra: ')).upper().strip()
palavras = texto.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print('A frase "{}", ao contário fica "{}".\n'.format(junto, inverso))

if junto == inverso:
    print('É UM PALÍNDROMO!')
else:
    print('NÃO É UM PALÍNDRMO')