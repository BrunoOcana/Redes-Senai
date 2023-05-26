# Criando uma função
def somar(n1, n2, n3=0, n4=0):
    total_soma = n1 + n2 + n3 + n4
    return total_soma

def subtrair(n1, n2, n3=0, n4=0):
    total_sub = n1 - n2 - n3 - n4
    return total_sub

def mult(n1, n2, n3=1, n4=1):
    total_mult = n1 * n2 * n3 * n4
    return total_mult

def div(n1, n2, n3=1, n4=1):
    total_div = n1 / n2 / n3 / n4
    return total_div

# É necessário DEFinir uma função usando o "def" seguido do nome da função
# e suas variáveis. Essas variáveis podem ser presas dentro da função.

# Veja que é necessário que a função "retorne" um valor, ou seja, um resultado.
# Esse valor pode ser qualquer coisa, inclusive uma outra operação ou um texto.

while True:
    print("Faça a sua operação!\nSoma: 1;   Subtração: 2;   Multiplicação: 3;   Divisão: 4.")
    escolha = int(input("Escolha: "))

    print("Quais números serão usados?")
    n1 = float(input("Primeiro: "))
    n2 = float(input("Segundo: "))
    n3 = float(input("Terceiro (0 para anular): "))
    n4 = float(input("Quarto (0 para anular): "))
    

    if escolha == 1:
        if n3 != 0 and n4 != 0:
            result = somar(n1,n2,n3,n4)
            print(f"O resultado é: {result}")
        elif n3 != 0:
            result = somar(n1,n2,n3)
            print(f"O resultado é: {result}")
        else:
            result = somar(n1,n2)
            print(f"O resultado é: {result}")
    elif escolha == 2:
        if n3 != 0 and n4 != 0:
            result = subtrair(n1,n2,n3,n4)
            print(f"O resultado é: {result}")
        elif n3 != 0:
            result = subtrair(n1,n2,n3)
            print(f"O resultado é: {result}")
        else:
            result = subtrair(n1,n2)
            print(f"O resultado é: {result}")
    elif escolha == 3:
        if n3 != 0 and n4 != 0:
            result = mult(n1,n2,n3,n4)
            print(f"O resultado é: {result}")
        elif n3 != 0:
            result = mult(n1,n2,n3)
            print(f"O resultado é: {result}")
        else:
            result = mult(n1,n2)
            print(f"O resultado é: {result}")
    elif escolha == 4:
        if n3 != 0 and n4 != 0:
            result = div(n1,n2,n3,n4)
            print(f"O resultado é: {result}")
        elif n3 != 0:
            result = div(n1,n2,n3)
            print(f"O resultado é: {result}")
        else:
            result = div(n1,n2)
            print(f"O resultado é: {result}")
    else:
        print("Operação não existente.")
    
    print("Gostaria de realizar outro cálculo? Sim: 1;  Não: 2.")
    repetir = int(input("Repetir: "))

    if repetir == 2:
        print("Até a próxima.")
        break
    elif repetir != 1:
        print("Escolha inválida.")
        break
    else:
        print("Ok. Vamos lá.")
