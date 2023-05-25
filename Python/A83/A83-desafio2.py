# Crie um programa em Python que mostre na tela todos os números pares que estão
# no intervalo de 1 a 60.

print("Você quer contar até um número?")
escolha = str(input("Sua resposta (Sim ou Não): "))
num = int(input("Contar até: "))

if escolha.lower() == "sim":
    for c in range(0,num+1,2):
        print(c)
else:
    print("Ok...")

if escolha.lower() == "sim":
    print("\nInfelizmente eu só gosto de números pares >:D")

print ("\nAté a próxima.")