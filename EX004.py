# Tipos primitivos
# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
n = input("Digite algo: ")
print("O tpo primitivo dessa variável é:", type(n))
print('É só tem números? ', n.isnumeric()) #Se for numerico, será True. Senão, será False
print('Tem só letras?', n.isalpha()) # Se for letra
print('Está tudo em letras maiúsculas?', n.isupper()) # Se está tudo com letras MAIUSCULAS
print('Não começa com números e não contém espaços?', n.isidentifier())
print('Está tudo em letras minúsculas?', n.islower())
print("Está capitalizada?", n.istitle()) # letras mAisCUls e MiNusCULas





