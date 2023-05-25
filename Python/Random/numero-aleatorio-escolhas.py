# Ideia: Criar uma forma de interagir com o usuário, com diversas opções.
import random

# Funções
def calculo(val,val2,rg):
    if rg != 0:
        if val2 != 0:
            cl = round((val + val2) * random.choice(range(1,rg+1)) / random.choice(range(1,rg+1)) ,2)
            return cl
        else:
            cl = round(val * random.choice(range(1, rg+1)) ,2)
            return cl
    elif val2 != 0:
        cl = val * val2 - 13 * (1/val2)
        return cl
    else:
        animais = ["Gamba(s)","Girafa(s)","doninha(s)"]
        cl = str(f"{val * random.choice(range(1,11))} {random.choice(animais)}.")
        return cl

print("Olá. Você gostaria de uma resposta aleatória?")
escolha = input("Sim ou não: ")

while True:
	if escolha.lower() == "sim" or escolha.lower() == "s":
		e1 = int(input("Escolha um número: "))
		e2 = int(input("Escolha outro número (0 para pular): "))
		e3 = int(input("Escolha um nível de aleatoriedade (0 para pular): "))
		resposta = calculo(e1,e2,e3)
		print (f"Sua resposta aleatória é: {resposta}.")
		e4 = input("Você gostaria de repetir o processo?\nSim ou não: ")
		if e4.lower() == "não" or escolha.lower() == "n":
			print ("Até a próxima.")
			break
		elif e4.lower() == "sim" or escolha.lower() == "s":
			print ("Então bora!")
		else:
			del escolha
			print("Sua respostan não condiz com o padrão. Tente novamente.")
			escolha = input("Sim ou não: ")
	elif escolha.lower() == "não" or escolha.lower() == "n":
		print("Até a próxima.")
		break
	else:
		del escolha
		print("A sua resposta está fora do padrão.\nTente novamente.")
		escolha = input("Sim ou não: ")