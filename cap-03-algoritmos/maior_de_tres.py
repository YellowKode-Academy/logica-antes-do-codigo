# Capítulo 3 — Algoritmos: Encontrar o maior de três números
#
# Pseudocódigo:
#   RECEBER numero1, numero2, numero3
#   SE numero1 >= numero2 E numero1 >= numero3
#       maior = numero1
#   SENÃO SE numero2 >= numero3
#       maior = numero2
#   SENÃO
#       maior = numero3
#   MOSTRAR maior

print("=== Maior de Três Números ===")

# Entrada
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

# Processamento
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3:
    maior = n2
else:
    maior = n3

# Saída
print(f"O maior número é: {maior}")
