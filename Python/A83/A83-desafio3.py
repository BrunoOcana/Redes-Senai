# Crie um programa que utilize o laço de repetição "for" para mostrar a tabuada
# de um número escolhido pelo usuário, como o exemplo: n * 2 = 2n.

print("Você quer saber a tabuada de um número?")
num = int(input("Qual número: "))

for tabs in range(1,11):
    print(f"{num} * {tabs} = {num*(tabs)}")