#Crie um programa que escreva "Olá mundo!" na tela.

print("Olá mundo!")

frase = 'Seja bem vindo(a) ao Python!'
print(frase)

# EX002 - Respondendo ao usuário

nome = input('Digite seu nome: ')
print("Nice to meet you ", nome, "!")
print("O que você deseja fazer {}?".format(nome))

# EX 003 - Somar valores

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um segundo valor: "))
soma = num1+num2
print("A soma de {} e {} é {}: ".format(num1, num2, soma)) #Nova Sintaxe

# EX004 - Dissecando uma variável

n1 = int(input('Digite um valor'))
print(type(n1))



