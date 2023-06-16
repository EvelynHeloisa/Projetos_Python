while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro núumero: '))
        r = a / b
    except Exception as erro:
        print('='*60)
        print(f'\033[31mTivemos um problema!\nProblema encontrado : {erro}\nTente novamente!\033[m')
        print('='*60)
    else:
        print(f'O resultdo de {a} divido por {b} é {r:.2f}')
        break

        