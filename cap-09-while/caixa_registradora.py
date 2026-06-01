# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 9 - While: Repetindo Ate Acontecer
# Snippet: segundo exemplo - caixa registradora com leitura antecipada
# ============================================================

# acumulador do total da compra
total = 0

print("=== Caixa Registradora ===")
print("Digite o valor de cada item. Digite 0 para encerrar.")

# le o primeiro item antes do loop
entrada = input("Valor do item: ")
valor_item = float(entrada)

# continua enquanto o operador nao digitar 0
while valor_item != 0:
    total = total + valor_item
    print(f"Subtotal: R${total:.2f}")

    # le o proximo item ao final de cada iteracao
    entrada = input("Valor do item (0 para encerrar): ")
    valor_item = float(entrada)

print(f"\nTotal da compra: R${total:.2f}")
