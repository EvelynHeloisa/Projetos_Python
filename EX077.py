palavras = ('Manje', 'Bouyon', 'Ji', 'Grenadya',
            'Renmen', 'Solèy', 'Chat', 'Fason',
            'Koute',)

for p in palavras:
    print(f'\nVogais na palavra {p}:', end=' ')
    for letra in p:
        if letra in 'aeèiòu':
            print(letra, end=' ')
