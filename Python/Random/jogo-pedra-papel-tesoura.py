#Escolha do computador
import random

#Estrutura
def jogo_escolhas():
    EJ = input("digite pedra, papel ou tesoura: ")
    PPT = ["pedra", "papel", "tesoura"]
    EC = random.choice(PPT)
    escolhas = {"jogador": EJ, "computador": EC}
    return escolhas

def verificando(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif jogador == "papel":
        if computador == "tesoura":
            return "Você perdeu..."
        else:
            return "Você ganhou!"
    elif jogador == "pedra":
        if computador == "papel":
            return "Você perdeu..."
        else:
            return "Você ganhou!"
    else:
        if computador == "pedra":
            return "Você perdeu..."
        else:
            return "Você ganhou!"

#Resultado
escolhas = jogo_escolhas()
resultado = verificando(escolhas["jogador"],escolhas["computador"])
print(escolhas)
print(resultado)