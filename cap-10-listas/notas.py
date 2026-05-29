# Capítulo 10 — Listas: Calculadora de Média com Notas

print("=== Calculadora de Média ===")

notas = []
quantidade = 5

# Coleta as notas
for i in range(1, quantidade + 1):
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)

# Cálculo
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

# Resultado
print()
print(f"Notas registradas: {notas}")
print(f"Média: {media:.1f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")

# Classificação
if media >= 7:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")
