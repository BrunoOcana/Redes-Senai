# Escreva uma função chamada verificar_par que recebe um número inteiro como
# argumento e verifica se o número é par ou não. A função deve retornar True se o
# número for par e False caso contrário. Em seguida, chame a função com diferentes
# valores e imprima o resultado.

def verif_par(n1):
    if n1 % 2 == 0:
        return True
    else:
        return False
    
print("\nVerifique se o número é par.")
numero = int(input("Escolha: "))

if verif_par(numero) is True:
    print("É um número par.")
else:
    print("Não é um número par.")