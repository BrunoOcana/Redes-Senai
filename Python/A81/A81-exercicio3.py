# Desenvolva um algoritmo que leia três notas de um aluno,
# calcule e exiba sua média

#Input dos dados
print ("""Olá usuário.
Verifique qual é média de suas notas. Separe decimais com pontos""")
n1 = float(input("""Qual o valor da primeira prova?
"""))
n2 = float(input("""Qual o valor da segunda prova?
"""))
n3 = float(input("""Qual o valor da terceira prova?
"""))

#Cálculo
total = round((n1 + n2 + n3)/3, 2)

#Verificação & retorno
if total >= 6:
    print (f"Parabéns, você passou! \nSua média foi {total}.")
elif total >= 5:
    print ("Você será encaminhado para o conselho de classe.")
    print (f"Sua média foi de: {total}")
else:
    print (f"Infelizmente você reprovou nesta matéria. \n Sua nota foi {total}")