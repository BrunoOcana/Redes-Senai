# Crie um programa para ler a temperatura em Celsius e apresentar a
# temperatura convertida em Farenheit. A fórmula para conversão: F=(9*C+160)/5

print ("""Olá usuário.
Você quer verificar qual é a conversão da temperatura para retarded units?""")
cels = float(input("""Informe, por favor, qual é a temperatura em Celsius:
Temperatura: """))
faren = round((9 * cels + 160) / 5, 2)
temp = {"Celsius" : cels, "Farenheit" : faren}

#Resultado
print (f"A temperatura {cels}ºC em Farenheit é de {faren}ºF.")