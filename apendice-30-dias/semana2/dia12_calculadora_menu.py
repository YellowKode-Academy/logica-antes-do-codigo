# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 12 - Programa com menu: calculadora interativa
# ============================================================

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

while True:
    print("\n=== Calculadora ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "0":
        print("Encerrando.")
        break

    if opcao not in ("1", "2", "3", "4"):
        print("Opcao invalida.")
        continue

    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))

    if opcao == "1":
        print(f"Resultado: {somar(a, b)}")
    elif opcao == "2":
        print(f"Resultado: {subtrair(a, b)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcao == "4":
        resultado = dividir(a, b)
        if resultado is None:
            print("Erro: divisao por zero.")
        else:
            print(f"Resultado: {resultado}")
