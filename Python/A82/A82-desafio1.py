# Desenvolva um programa que leia a ideade de uma pessoa e informe se ela é
# maior ou menor que 18 anos.

user = input("Por favor, informe seu nome.")
print(f"Olá {user}, por favor verifique sua idade.")

idade = input("Idade: ")

if idade >= 18:
    print ("Você pode acessar o site normalmente.")
elif idade < 18:
    print ("Você não pode acessar o conteúdo desse site.")