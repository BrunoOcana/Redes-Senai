# Desenvolva um algoritmo que leia três notas de um aluno,
# calcule e exiba sua média

print ("""Olá usuário.
Verifique qual é média de suas notas. Separe decimais com pontos""")
n1 = float(input("""Qual o valor da primeira prova?
"""))
n2 = float(input("""Qual o valor da segunda prova?
"""))
n3 = float(input("""Qual o valor da terceira prova?
"""))

total = round((n1 + n2 + n3)/3, 2)

if total >= 6:
    print (f"Parabéns, você passou! \n Sua nota foi {total}")
else:
    print (f"Infelizmente você reprovou nesta matéria. \n Sua nota foi {total}")