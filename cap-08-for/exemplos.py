# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 8 - Repeticao com FOR
# Snippet: agregado das tres variacoes de for - referencia rapida
# ============================================================
# O for percorre uma sequencia de valores

print("=== Contagem de 1 a 10 ===")
for numero in range(1, 11):
    print(numero, end=" ")
print()  # quebra de linha

print()

# Exercicio do capitulo: soma de 1 a 100
print("=== Soma de 1 a 100 ===")
total = 0
for n in range(1, 101):
    total = total + n
print(f"A soma de 1 a 100 e: {total}")

print()

# Tabela de multiplicacao
print("=== Tabuada do 7 ===")
for i in range(1, 11):
    resultado = 7 * i
    print(f"7 x {i:2d} = {resultado}")
