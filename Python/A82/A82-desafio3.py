# Escreva um programa que pergunte o salário de um funcionário do SENAI
# e calcule o valor do seu aumento. Para salários superiores a R$8250,00
# calcule um aumento de 10%. Para os inferiores ou iguais, calcule um
# aumento de 15%.

print(f"Olá.")
senai = input("Você trabalha no SENAI? (Sim ou Não) \nResposta: ")

def reajuste(salario):
    if salario > 8250:
        sal_ajustado = round(salario * 1.10)
        return sal_ajustado
    else:
        sal_ajustado = round(salario * 1.15)
        return sal_ajustado

if senai == "Sim" or senai == "sim":
    print("Vamos verificar qual o reajuste do seu salário.")
    sal = float(input("Informe seu salário: "))
    sal_novo = reajuste(sal)
    print (f"\nSeu salário ajustado é de: R${sal_novo}.")
    
else:
    print("Você não está qualificado para verificar o reajuste.")

