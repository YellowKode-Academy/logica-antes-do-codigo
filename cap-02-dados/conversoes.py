# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 2 - Dados Sao Informacao
# Snippet: conversoes explicitas entre tipos (int, float, str, bool)
# ============================================================

# int("42") converte string para inteiro
print(int("42"))           # 42

# float("9.90") converte string para float
print(float("9.90"))       # 9.9

# str(42) converte inteiro para string
print(str(42))             # "42" (mas o print mostra 42)

# bool(0) e bool(1)
print(bool(0))             # False
print(bool(1))             # True
print(bool(42))             # True - qualquer numero diferente de 0 e True
