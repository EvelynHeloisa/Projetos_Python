sexo = str(input('Digite o seu sexo [F/M]: ')).strip().upper()[0] #Somente a primeira letra

while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido! Infome novamente [F/M]: '))
print('Dados registrados com sucesso!')