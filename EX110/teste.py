import moeda

moe = float(input('Digite um valor em real R$: '))
print(f'{moeda.moeda(moe)} aumentando 10% é {moeda.moeda(moeda.aumentar(moe, 10))}')
print(f'Diminuindo 15% é {moeda.moeda(moeda.diminuir(moe, 15))}')
print(f'O dobro é {moeda.moeda(moeda.dobro(moe))}')
print(f'A metade é {moeda.moeda(moeda.metade(moe))}')
