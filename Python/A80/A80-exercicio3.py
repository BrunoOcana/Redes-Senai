#Variables
print ("Olá querido aluno. Informe abaixo seus dados:")
Nome = input("Qual o seu nome completo: ")
NDia, NMes, NAno = input("Qual a sua data de nascimento (dia,mês,ano):").split(",",2)

#Code
print ("Seja bem-vindo,", Nome)
print ("Você nasceu em {} do {} de {}.".format(NDia,NMes,NAno))