def fatorial(num, show=False):
    """
    -> Função para calcular o fatorial
    :param num: número a ser calculado
    :param show: variavél lógica para mostrar o cálculo ou não
    :return: sem reorno (pois não entendi muito bem essa parte)
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)


print('='*30)
print(f'{"CALCULANDO O FATORIAL":^30}')
print('='*30)

n = int(input('Digite um número: '))
show = False
resp = str(input('Deseja mostar o cálculo? [S/N] ')).strip().upper()[0]
if resp == 'S':
    show = True
elif resp == ' ':
    show = False

fatorial(n, show)


