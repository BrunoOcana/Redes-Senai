# Escreva um programa que leia a velocidade de um carro. Se o carro estiver
# mais rápido que 80km/h, mostre uma mensagem dizendo que ele foi multado.

print(f"Olá, por favor informe sua velocidade ao passar pelo radar.")
vel = input("Velocidade: ")

if vel > 80:
    print (f"Você foi multado em R${vel / 100 * 500}.")
    print (f"Pagamento em até 1 semana!")
elif vel <= 80:
    print ("Você não sofreu nenhuma penalidade.")