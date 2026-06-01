# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 10 - Listas: Guardando Varios Valores
# Snippet: exercicio resolvido - 3 amigos ordenados alfabeticamente
# ============================================================

# cria lista vazia para os nomes
amigos = []

# coleta os 3 nomes
print("Digite os nomes de 3 amigos:")
for i in range(1, 4):
    nome = input(f"Amigo {i}: ")
    amigos.append(nome)

# ordena em ordem alfabetica
amigos.sort()

# exibe os nomes numerados
print("\nLista em ordem alfabetica:")
for posicao in range(len(amigos)):
    print(f"{posicao + 1}. {amigos[posicao]}")

# versao alternativa com enumerate
print("\nVersao com enumerate:")
for posicao, nome in enumerate(amigos, start=1):
    print(f"{posicao}. {nome}")
