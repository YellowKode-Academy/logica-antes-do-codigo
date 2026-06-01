# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 8 - Repeticao com FOR
# ============================================================
# O for percorre uma sequência de valores

print("=== Contagem de 1 a 10 ===")
for numero in range(1, 11):
    print(numero, end=" ")
print()  # quebra de linha

print()

# Exercício do capítulo: soma de 1 a 100
print("=== Soma de 1 a 100 ===")
total = 0
for n in range(1, 101):
    total = total + n
print(f"A soma de 1 a 100 é: {total}")

print()

# Tabela de multiplicação
print("=== Tabuada do 7 ===")
for i in range(1, 11):
    resultado = 7 * i
    print(f"7 x {i:2d} = {resultado}")
