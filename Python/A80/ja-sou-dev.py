#Variables
Nome = input("Informe seu nome: ")
Idade = input("Informe sua idade em números: ")
Escola = "SENAI"
Rua = "Rua Niteroi, Nº 180"
Cidade = "São Caetano do Sul - SP"

#Localidade
#print ('A escola',Escola,"está localizada na",Rua + ", em",Cidade + ".")

print ("Olá {}. Você possui {} anos e está cursando no {}?".format(Nome,Idade,Escola))
print ("Confira a localização da instituição abaixo.")
print ("A escola {} está localizada na {}, em {}." .format(Escola,Rua,Cidade))