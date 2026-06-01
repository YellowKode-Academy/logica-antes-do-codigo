# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 8 - Repeticao: Fazendo o Computador Trabalhar por Voce
# Snippet: exercicio resolvido - soma de 1 a 100 (Gauss)
# ============================================================

# acumulador comeca em zero
soma = 0

# percorre todos os numeros de 1 a 100
for numero in range(1, 101):
    soma = soma + numero

print(f"A soma de 1 a 100 e: {soma}")
