#Variables
print ("Olá querido aluno. Informe abaixo seus dados:")
Nome = input("Qual o seu nome completo: ")
while True:
    try:
        NDia, NMes, NAno = input("Qual a sua data de nascimento (dia,mês,ano):").split(",",2)
        if int(NDia) and int(NMes) and int(NAno):
            break
    except:
      print ("Valor inválido. Digite somente números inteiros.")


#Code
print ("Seja bem-vindo,", Nome)
print ("Você nasceu em {} do {} de {}.".format(NDia,NMes,NAno))