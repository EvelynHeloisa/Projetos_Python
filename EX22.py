frase = str(input('Digite uma frase: ')).strip().lower()
print('Essa frase possui {} letras A'.format(frase.count('a')))
print('A primeira letra A está na posição {} '.format(frase.find("a")+1))
print('A última letra A está na posição {}'.format(frase.rfind("a")+1))
