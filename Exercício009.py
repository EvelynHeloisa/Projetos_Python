# Tabuada

num = int(input("Digite um número para ver sua tabuada: "))
i = 1
min = int(input("Digite o fator mínino: "))
max = int(input("Digite o fator máximo: "))
while min <= max:
    print(num, " x ", min, " = ", num*min)
    min = min+1

if min < 0:
    print("Valor inválido! Tente novamente.")