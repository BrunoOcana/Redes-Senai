# Desenvolva um script em python que receba o salário de um funcionário
# e mostre seu novo salário, com 12% de reajuste.

print ("""Olá usuário.
Você quer verificar qual seria o reajuste do seu salário?""")
salb = float(input("""Informe, por favor, qual é o seu salário atual, usando ponto para separar os centavos.
Salário: R$"""))

reaj = int(input("""Informe, por favor, qual é o reajuste.
Reajuste: """))

aumento = reaj / 100
sala = round(salb + salb * aumento, 2)

print (f"""Este é o seu salário após o reaguste:
Salário: R${sala}""")