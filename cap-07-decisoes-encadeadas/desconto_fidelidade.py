# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 7 - Decisoes Encadeadas
# Snippet: sistema de descontos com AND - fidelidade vs boas-vindas
# ============================================================

# coleta os dados do cliente
anos = float(input("Ha quantos anos voce e cliente? "))
valor = float(input("Valor da compra (R$): "))

# verifica desconto de fidelidade (cliente antigo E compra alta)
if anos > 1 and valor > 100:
    desconto = valor * 0.15
    total = valor - desconto
    print(f"Desconto fidelidade aplicado: R${desconto:.2f}")
    print(f"Total a pagar: R${total:.2f}")

# verifica desconto de boas-vindas (cliente novo E compra muito alta)
elif anos <= 1 and valor > 200:
    desconto = valor * 0.05
    total = valor - desconto
    print(f"Desconto boas-vindas aplicado: R${desconto:.2f}")
    print(f"Total a pagar: R${total:.2f}")

# sem desconto
else:
    print("Sem desconto nesta compra.")
    print(f"Total a pagar: R${valor:.2f}")
