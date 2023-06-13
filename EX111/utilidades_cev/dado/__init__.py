def ler_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'ERRO! Opção inválida.')
        else:
            valido = True
            return float(entrada)


