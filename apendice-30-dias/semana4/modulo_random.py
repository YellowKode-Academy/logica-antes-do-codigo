# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 4 - Modulos da Biblioteca Padrao
# Snippet: import random - numeros aleatorios, escolhas, embaralhamento
# ============================================================

import random

numero = random.randint(1, 100)    # inteiro entre 1 e 100
decimal = random.uniform(0, 1)     # decimal entre 0 e 1
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)              # embaralha a lista no lugar
escolha = random.choice(lista)     # escolhe um elemento aleatorio

print(f"Inteiro aleatorio (1-100): {numero}")
print(f"Decimal aleatorio (0-1):   {decimal:.4f}")
print(f"Lista embaralhada:         {lista}")
print(f"Escolha aleatoria:         {escolha}")
