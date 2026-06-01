# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 8 - Repeticao: Fazendo o Computador Trabalhar por Voce
# Snippet: tres variacoes de for - contagem, tabuada e soma acumulada
# ============================================================

# variacao 1: contagem simples de 1 a 10
print("Contagem:")
for numero in range(1, 11):
    print(numero)

# variacao 2: tabuada do 7
print("\nTabuada do 7:")
for i in range(1, 11):
    resultado = 7 * i
    print(f"7 x {i} = {resultado}")

# variacao 3: soma acumulada dos numeros de 1 a 5
print("\nSoma acumulada:")
total = 0
for numero in range(1, 6):
    total = total + numero
    print(f"Adicionando {numero} -> total agora e {total}")

print(f"Soma final: {total}")
