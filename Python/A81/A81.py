#Variables
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

#Soma
if n1 >= n2:
    total = n1 + n2
elif n1 <= n2:
    total = n1 * (n2+2)
#Print
print (total)
print (type(total))