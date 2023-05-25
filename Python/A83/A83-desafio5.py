# Desenvolver um programa que calcule o Fatorial de um número digitado
# pelo usuário. Ex: 6 = 6 * 5 * 4 * 3 ... * 1 = 720

print("Você quer contar o fatorial de um número?")
escolha = str(input("Sua resposta (Sim ou Não): "))
num = int(input("Qual o valor: "))
valor = 1

if escolha.lower() == "sim":
    for c in range(num,0,-1):
        valor *= c
else:
    print("Ok...")

print (f"O valor final é de {valor}")