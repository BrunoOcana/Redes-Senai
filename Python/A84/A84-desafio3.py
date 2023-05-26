# Faça uma função que receba 3 parâmetros com valores reais. Seu programa deve
# analisar todos os valores e dizer qual é o maior deles.

def maior(n1=0, n2=0, n3=0):
    if n1 > n2 and n1 > n3:
        return print(f"O número {n1} é o maior deles.")
    elif n2 > n1 and n2 > n3:
        return print(f"O número {n2} é o maior deles.")
    elif n3 > n1 and n3 > n2:
        return print(f"O número {n3} é o maior deles.")
    elif n1 == n2:
        return print(f"O número {n3} é o menor.")
    elif n1 == n3:
        return print(f"O número {n2} é o menor.")
    else:
        return print(f"O número {n1} é o menor.")

while True:
    print("Olá. Compare 3 números.")
    n1 = float(input("Qual o primeiro número: "))
    n2 = float(input("Qual o segundo número: "))
    n3 = float(input("Qual o terceiro número: "))

    result = maior(n1, n2, n3)

    print("\nGostaria de realizar outro cálculo? Sim: 1;  Não: 2.")
    repetir = input("Repetir: ")

    try:
        repetir = int(repetir)
        if repetir != 1 and repetir != 2:
            print("\nEscolha inválida.")
            break
        elif repetir == 1:
            print("\nOk. Vamos lá.")
        else:
            print("\nAté a próxima.")
            break
    except:
        print("\nEscolha inválida.")
        break