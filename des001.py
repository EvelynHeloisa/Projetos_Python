#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

print("=====================================================")
print("               REAJUSTE DE SALÁRIOS")
print(" ")

sal_atual = float(input("Digite seu salário atual: R$: "))

if sal_atual >= 1500.00:
    porcentual = sal_atual * 0.5
    sal_pos = sal_atual + porcentual
    print("Aumento de 5%")
    print("Salário após o reajuste: R$", sal_pos)

if sal_atual >= 700 < 1500:
    porcentual = sal_atual * 0.10
    sal_pos = sal_atual + porcentual
    print("Aumento de 10%")
    print("Salário após o reajuste: R$", sal_pos)

elif sal_atual >= 280 < 700:
    porcentual = sal_atual * 0.15
    sal_pos = sal_atual + porcentual
    print("Aumento de 15%")
    print("Salário após o reajuste: R$", sal_pos)

if sal_atual < 280:
    porcentual = sal_atual * 0.20
    sal_pos = sal_atual + porcentual
    print("Aumento de 20%")
    print("Salário após o reajuste: R$", sal_pos)