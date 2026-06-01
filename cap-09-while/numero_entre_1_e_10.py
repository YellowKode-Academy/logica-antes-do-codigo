# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 9 - While: Repetindo Ate Acontecer
# Snippet: exercicio resolvido - pedir numero entre 1 e 10 ate ser valido
# ============================================================

# inicia com um valor que garante entrada no loop
numero = 0

# continua enquanto o numero estiver fora do intervalo valido
while numero < 1 or numero > 10:
    entrada = input("Digite um numero entre 1 e 10: ")
    numero = int(entrada)

    # verifica se esta fora do intervalo e informa
    if numero < 1 or numero > 10:
        print(f"{numero} nao e um valor valido. O numero deve estar entre 1 e 10.")

# chegou aqui: o numero e valido
print(f"Numero valido recebido: {numero}")
