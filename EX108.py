import moeda

moe = float(input('Digite um valor em real R$: '))
print(f'{moeda.moeda(moe)} aumentando 10% é R${moeda.aumentar(moe, 10):.2f}')
print(f'Diminuindo 15% é R${moeda.diminuir(moe, 15):.2f}')
print(f'O dobro é R${moeda.dobro(moe):.2f}')
print(f'A metade é R${moeda.metade(moe):.2f}')
