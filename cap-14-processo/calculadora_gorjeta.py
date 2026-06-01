# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 14 - Do Pseudocodigo ao Python
# ============================================================
#
# PROBLEMA: Calculadora de gorjeta
#
# PASSO 1 - Entender o problema:
#   Entrada: valor da conta, percentual de gorjeta
#   Saída: valor da gorjeta, total a pagar
#
# PASSO 2 - Exemplos concretos:
#   Conta R$100, gorjeta 10% → gorjeta R$10, total R$110
#   Conta R$85,  gorjeta 15% → gorjeta R$12.75, total R$97.75
#   Conta R$200, gorjeta 20% → gorjeta R$40, total R$240
#
# PASSO 3 - Pseudocódigo:
#   RECEBER valor_conta
#   RECEBER percentual_gorjeta
#   gorjeta = valor_conta * (percentual_gorjeta / 100)
#   total = valor_conta + gorjeta
#   MOSTRAR gorjeta, total
#
# PASSO 4 - Estruturas necessárias:
#   Variáveis (float), operações aritméticas, print formatado
#
# PASSO 5 - Código:

def calcular_gorjeta(valor_conta, percentual):
    """Calcula gorjeta e total da conta."""
    gorjeta = valor_conta * (percentual / 100)
    total = valor_conta + gorjeta
    return gorjeta, total

print("=== Calculadora de Gorjeta ===")
conta = float(input("Valor da conta (R$): "))
percentual = float(input("Percentual de gorjeta (%): "))

gorjeta, total = calcular_gorjeta(conta, percentual)

print()
print(f"Conta:   R${conta:.2f}")
print(f"Gorjeta: R${gorjeta:.2f} ({percentual:.0f}%)")
print(f"Total:   R${total:.2f}")

# PASSO 6 - Testar com os exemplos do Passo 2:
print()
print("--- Testes automáticos ---")
for conta_teste, perc_teste, esperado in [(100, 10, 110), (85, 15, 97.75), (200, 20, 240)]:
    g, t = calcular_gorjeta(conta_teste, perc_teste)
    status = "OK" if abs(t - esperado) < 0.01 else "ERRO"
    print(f"R${conta_teste} + {perc_teste}% = R${t:.2f} [{status}]")
