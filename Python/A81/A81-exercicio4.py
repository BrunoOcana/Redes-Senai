# Crie um programa que receba um valor em metros e exiba-o convertendo
# em centímetros e milímetros

print ("""Olá usuário.
Verifique qual é o valor de metros em centímetros e milímetros.""")
n1 = float(input("""Qual a medida em metros (Ex: 103.5)?
"""))

#float(n1 = str.replace(",", "."))


cent = n1 * 100
mili = n1 * 1000

print (f"""Esses são os valores:
Centímetros: {cent} cm
Milímetros: {mili} mm""")