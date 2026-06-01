# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 14 - Projeto de revisao: conversor de medidas com menu
# ============================================================

def converter_comprimento(valor, origem, destino):
    # tudo em metros como base
    para_metros = {"km": 1000.0, "m": 1.0, "cm": 0.01}
    if origem not in para_metros or destino not in para_metros:
        return None
    em_metros = valor * para_metros[origem]
    return em_metros / para_metros[destino]

def converter_massa(valor, origem, destino):
    para_gramas = {"kg": 1000.0, "g": 1.0}
    if origem not in para_gramas or destino not in para_gramas:
        return None
    em_gramas = valor * para_gramas[origem]
    return em_gramas / para_gramas[destino]

def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

while True:
    print("\n=== Conversor de Medidas ===")
    print("1 - Comprimento (km, m, cm)")
    print("2 - Massa (kg, g)")
    print("3 - Temperatura (C, F)")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "0":
        break

    if opcao == "1":
        origem = input("Unidade de origem (km, m, cm): ")
        destino = input("Unidade de destino (km, m, cm): ")
        valor = float(input("Valor: "))
        resultado = converter_comprimento(valor, origem, destino)
        if resultado is None:
            print("Unidades invalidas.")
        else:
            print(f"{valor} {origem} = {resultado} {destino}")
    elif opcao == "2":
        origem = input("Unidade de origem (kg, g): ")
        destino = input("Unidade de destino (kg, g): ")
        valor = float(input("Valor: "))
        resultado = converter_massa(valor, origem, destino)
        if resultado is None:
            print("Unidades invalidas.")
        else:
            print(f"{valor} {origem} = {resultado} {destino}")
    elif opcao == "3":
        direcao = input("Converter de (1) Celsius para Fahrenheit ou (2) Fahrenheit para Celsius? ")
        valor = float(input("Valor: "))
        if direcao == "1":
            print(f"{valor}C = {celsius_para_fahrenheit(valor):.2f}F")
        elif direcao == "2":
            print(f"{valor}F = {fahrenheit_para_celsius(valor):.2f}C")
        else:
            print("Opcao invalida.")
    else:
        print("Opcao invalida.")
