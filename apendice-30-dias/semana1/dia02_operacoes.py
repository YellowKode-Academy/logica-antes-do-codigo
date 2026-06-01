# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 1
# Dia 2 - Tipos e conversao: quatro operacoes aritmeticas
# ============================================================

a = float(input("Primeiro numero: "))
b = float(input("Segundo numero: "))

print(f"Soma:         {a + b}")
print(f"Subtracao:    {a - b}")
print(f"Multiplicacao: {a * b}")
if b != 0:
    print(f"Divisao:      {a / b}")
else:
    print("Divisao:      indefinida (divisor zero)")
