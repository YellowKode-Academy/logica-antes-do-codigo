# Capítulo 5 — Sequência: Calculadora de Troco
# Padrão: Entrada → Processamento → Saída

print("=== Calculadora de Troco ===")

# ENTRADA
preco = float(input("Preço do produto (R$): "))
pagamento = float(input("Valor pago (R$): "))

# PROCESSAMENTO
troco = pagamento - preco

# SAÍDA
if troco < 0:
    print(f"Valor insuficiente. Faltam R${abs(troco):.2f}")
elif troco == 0:
    print("Pagamento exato. Sem troco.")
else:
    print(f"Troco: R${troco:.2f}")
