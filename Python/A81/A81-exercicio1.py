# Crie um programa que leia um número inteiro
# e mostre na tela seu sucessor e seu antecessor

print ("""Olá usuário.
Verifique qual é o sucessor e seu antecessor do seu número.""")
n1 = int(input("""Qual o número?
"""))

succ = n1 + 1
ante = n1 - 1

print (f"""Esses são os valores:
Sucessor: {succ}
Antecessor: {ante}""")