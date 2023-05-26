# Faça uma função que recebe um número inteiro positivo como argumento e imprime
# uma contagem regressiva a partir desse número até 0. Utilize o laço de repetição
# de sua preferência para realizar a contagem regressiva.

import time

# Função cronometro
def crono():
    ini = round(float(input("Quantos segundos: ")))
    for c in range(ini,-1,-1):
        print(f"{c}s")
        time.sleep(1)
    return print("fim.")

while True:
    print("\nOlá!\nExecute um cronômetro.")
    count = crono()
    escolha = input("Gostaria de repetir?\nSim ou não: ")
    #esclib = {"sim" : 1, "s" : 1 , "não" : 2 , "n" : 2}
    if escolha.lower() == "sim":
        print("Vamos lá!")
    elif escolha.lower() == "não":
        print("Até a próxima.")
        break
    else:
        print("resposta inválida.")
        break

