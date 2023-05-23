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
n4 = float(input("""Qual o valor da quarta prova?
"""))

total = round((n1 + n2 + n3 + n4)/4, 2)

print (f"""Esta é a sua média:
Média: {total}""")