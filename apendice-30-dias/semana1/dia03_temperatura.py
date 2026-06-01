# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 1
# Dia 3 - Condicionais simples: classificar temperatura
# ============================================================

temp = float(input("Temperatura em Celsius: "))

if temp < 15:
    print("Esta frio")
elif temp <= 25:
    print("Temperatura agradavel")
else:
    print("Esta quente")
