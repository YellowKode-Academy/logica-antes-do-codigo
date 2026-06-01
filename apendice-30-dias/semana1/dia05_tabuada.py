# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 1
# Dia 5 - Loop for: tabuada completa de um numero
# ============================================================

n = int(input("Numero para a tabuada: "))

print(f"\nTabuada do {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
