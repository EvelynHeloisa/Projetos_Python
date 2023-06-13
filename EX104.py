def leiaint(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro!\033[m')
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o valor {n}')

