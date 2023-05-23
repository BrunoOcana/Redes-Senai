# Crie um algoritmo que leia um número e mostre sua metade
# dobro e triplo

print ("""Olá usuário.
Verifique qual é a metade, o dobro e o triplo do seu número.""")
n1 = float(input("""Qual o número? (Use ponto para separar os decimais)
"""))

met = round(n1 / 2, 2)
dob = round(n1 * 2, 2)
trip = round(n1 * 3, 2)

print (f"""Esses são os valores:
Metade: {met}
Dobro: {dob}
Triplo: {trip}""")