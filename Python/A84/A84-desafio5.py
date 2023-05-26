# Crie um programa que leia dois valores e mostre um menu na tela com as opções:
# a. Somar   b. Multiplicar   c. Maior número   d. Menor número

def somar(n1, n2):
    total_soma = n1 + n2
    return total_soma

def mult(n1, n2):
    total_mult = n1 * n2
    return total_mult

def maior(n1, n2):
    total_max = max(n1, n2)
    return total_max

def menor(n1, n2):
    total_min = min(n1, n2)
    return total_min

def verif(escolha):
    if escolha not in vvalido[0:5]:
        return print("Escolha inválida.") 
    elif escolha == 1:
        resultado = somar(n1, n2)
        return print(f"O valor final é: {resultado}")
    elif escolha == 2:
        resultado = mult(n1, n2)
        return print(f"O valor final é: {resultado}")
    elif escolha == 3:
        resultado = maior(n1, n2)
        return print(f"O maior valor é: {resultado}")
    elif escolha == 4:
        resultado = maior(n1, n2)
        return print(f"O maior valor é: {resultado}")


while True:
    print("Faça a sua operação!\nSoma: 1;   Multiplicação: 2;   Maior: 3;   Menor: 4;   Sair: 5.")
    escolha = int(input("Escolha: "))
    vvalido = [1,2,3,4,5]

    if escolha == 5:
        break

    print("Quais números serão usados?")
    n1 = float(input("Primeiro: "))
    n2 = float(input("Segundo: "))

    resultado = verif(escolha)
    del escolha