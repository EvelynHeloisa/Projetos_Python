def leiaint(msg):
    while True:
        try:
            inte = int(input(msg))
        except Exception as erro:
            print('\033[31mDigite um número inteiro válido!\033[m')
        else:
            break
    return inte


def leiareal(msg):
    while True:
        try:
            real = float(input(msg))
        except Exception as erro:
            print('\033[31mDigite um número real válido!\033[m')
        else:
            break
    return real


inte = leiaint('Digite um número inteiro: ')
real = leiareal('Digute um número real: ')

print('='*50)
print(f'Você acabou de digitar o valor inteiro \033[7;34m {inte} \033[m e o valor real \033[7;34m {real} \033[m')


