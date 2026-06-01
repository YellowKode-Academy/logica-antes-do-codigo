# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 10 - Listas: Guardando Varios Valores
# Snippet: programa central - 5 notas, media, max, min e ordenacao
# ============================================================

# cria uma lista vazia para armazenar as notas
notas = []

# coleta 5 notas do usuario e adiciona na lista
print("Digite as 5 notas do aluno:")
for i in range(1, 6):
    entrada = input(f"Nota {i}: ")
    nota = float(entrada)
    notas.append(nota)  # adiciona o valor ao final da lista

# calcula estatisticas com as funcoes nativas do Python
total = sum(notas)        # soma todos os valores da lista
quantidade = len(notas)   # conta quantos itens ha na lista
media = total / quantidade
maior_nota = max(notas)   # encontra o valor mais alto
menor_nota = min(notas)   # encontra o valor mais baixo

# exibe os resultados
print(f"\nNotas registradas: {notas}")
print(f"Media: {media:.1f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")

# ordena a lista do menor para o maior
notas.sort()
print(f"Notas em ordem crescente: {notas}")
