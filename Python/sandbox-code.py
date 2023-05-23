#Verificando valores
N1 = "Olá"
N2 = 37
if type(N1) == str and type(N2) == int:
    print ("Combinação correta.")
elif type(N1) == str or type(N2) == int:
	print ("Um dos valores está correto.")
else:
	print ("Deu ruim.")

#Print em formato de tabela
N1, N2, N3, N4, N5, N6, N7, N8, N9 = input("Digite 9 valores aleatórios! ").split(" ",8)
print(f"""{N1}  {N2}  {N3}
{N4}  {N5}  {N6}
{N7}  {N8}  {N9}""")