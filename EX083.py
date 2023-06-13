pilha = []

expressao = str(input('Digite uma expressão: '))

for car in expressao:
    if car == '(':
        pilha.append('(')
    elif car == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada...')
    
