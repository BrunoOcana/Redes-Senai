# Aprender formas de repetir um código

# Pode ser usado a função for + in range para criar loops
print("Você quer saber quanto teria, a cada dia, se recebesse R$237/dia?")
escolha = str(input("Sua resposta (Sim ou Não): "))

# Avaliação da escolha
if (escolha.lower()) == "sim":
    for m in range(1,31):
        print (f"R$",237*m)
else:
    print("Ok...")