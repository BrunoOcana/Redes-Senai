# Crie um programa em Python que leia um número inteiro qualquer e mostre
# na tela a sua tabuada.

print ("""Olá usuário.
Verifique qual é a tabuada deste número.""")
n1 = int(input("""Qual o número?
"""))

if n1 > 10 or n1 < 1:
    print ("Tente um número entre 1 e 10")
else:
    n11 = n1 * 1
    n12 = n1 * 2
    n13 = n1 * 3
    n14 = n1 * 4
    n15 = n1 * 5
    n16 = n1 * 6
    n17 = n1 * 7
    n18 = n1 * 8
    n19 = n1 * 9
    n110 = n1 * 10

    print (f"""fEsta é a tabuada do número {n1}:
    {n11}  {n12}  {n13}  {n14}  {n15}
    {n16}  {n17}  {n18}  {n19}  {n110}""")