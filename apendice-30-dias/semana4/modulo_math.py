# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 4 - Modulos da Biblioteca Padrao
# Snippet: import math - sqrt, pow, pi, ceil, floor
# ============================================================

import math

raiz = math.sqrt(16)        # 4.0 - raiz quadrada
potencia = math.pow(2, 10)  # 1024.0 - 2 elevado a 10
pi = math.pi                # 3.14159...
teto = math.ceil(4.2)       # 5 - arredonda para cima
chao = math.floor(4.8)      # 4 - arredonda para baixo

print(f"sqrt(16):     {raiz}")
print(f"pow(2, 10):   {potencia}")
print(f"pi:           {pi:.5f}")
print(f"ceil(4.2):    {teto}")
print(f"floor(4.8):   {chao}")
