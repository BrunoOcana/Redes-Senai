# Faça um program que tenha uma funão chamada area() , que receba as dimensões
# de um terreno retangular (largura e comprimento e mostra a área do terreno).

import math

# Função Lado x Lado
def area(lado1, lado2):
    total_area = lado1 * lado2
    return round(total_area,2)

def areacir(raio):
    total_area = raio**2 * math.pi
    return round(total_area,2)

def volbox(compr, profun, altura):
    total_volbox = compr * profun * altura
    return round(total_volbox,2)

def volcil(raio, altura):
    basecil = raio**2 * math.pi
    total_volcil = basecil * altura
    return round(total_volcil,2)

while True:
    print("\nCalculadora de áreas e volumes!\nÁrea retangular: 1;   Área circular: 2;   Volume cubicular: 3;\nVolume cilíndrico: 4;  Sair: 5.")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        l1 = float(input("Qual a medida do lado 1: "))
        l2 = float(input("Qual a medida do lado 2: "))
        result = area(l1, l2)
        print(f"A área é de: {result}m².")
    elif escolha == 2:
        r1 = float(input("Qual a medida do raio: "))
        result = areacir(r1)
        print(f"A área é de: {result}m².")
    elif escolha == 3:
        l1 = float(input("Qual a medida do comprimento: "))
        p1 = float(input("Qual a medida da profundidade: "))
        a1 = float(input("Qual a medida da altura: "))
        result = volbox(l1, p1, a1)
        print(f"A área é de: {result}m³.")
    elif escolha == 4:
        r1 = float(input("Qual a medida do raio: "))
        a1 = float(input("Qual a medida da altura: "))
        result = volcil(r1, a1)
        print(f"A área é de: {result}m³.")
    elif escolha == 5:
        print("Tudo bem. Até a próxima.")
        break
    else:
        print("Operação inválida. Tente novamente.")