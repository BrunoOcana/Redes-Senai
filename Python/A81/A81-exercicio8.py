# Desenvolva um script em Python que receba um valor em reais (R$) e converta-o
# para dólares. Considere que $1 = R$4,91. No resultado, exiba apenas duas casas
# decimais após a vírgula.

print ("""Olá usuário.
Você quer verificar qual a conversão de um valor em reais para dólar?""")
brl = float(input("""Informe, por favor, qual é o valor em reais.
R$: """))

def converter():
    usd = round(brl / 4.91, 2)
    moedas = {"Real" : brl, "Dolar" : usd}
    return moedas

conversao = converter()
print("USD: {}".format(conversao["Dolar"]))