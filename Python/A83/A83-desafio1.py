# Crie um programa em Python que mostre na tela todos os números enter 1 e 60.

print("Você quer contar até um número?")
escolha = str(input("Sua resposta (Sim ou Não): "))
num = int(input("Contar até: "))

if escolha.lower() == "sim":
    for c in range(0,num+1):
        print(c)
else:
    print("Ok...")

print ("\nAté a próxima.")