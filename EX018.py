# LER O NOME COMPLETO DE UMA PESSOA E MOSTRAR
# 1) O NOME COM TODAS AS LETRAS MINUSCULAS
# 2) O NOME COM TODAS AS LETRAS MAIUSCULAS
# 3) QUANTAS LETRAS TEM AO TODO SEM CONSIDERAR OS ESPAÇOS
# 4) QUANTAS LETRAR TEM O PRIMEIRO NOME

print("="*30)
nome = str(input("Digite seu nome completo: ")).strip()
print("="*30)

print("TODAS AS LETRAs MAIÚSCULAS: ", nome.upper())
print("TODAS AS LETRAS MINÚSCULAS: ", nome.lower())
print("TOTAL DE LETRAS: ", len(nome.replace(" ", "")))
pri_nome = nome.split()
print('O primeiro nome "{}" tem {} letras'.format(pri_nome[0], len(pri_nome[0])))








