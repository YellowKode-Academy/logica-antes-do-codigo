# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 8 - Listas e loop: temperaturas da semana
# ============================================================

temperaturas = []

print("Digite 5 temperaturas (uma por dia):")
for i in range(1, 6):
    t = float(input(f"Temperatura dia {i}: "))
    temperaturas.append(t)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print(f"\nTemperaturas: {temperaturas}")
print(f"Media:        {media:.1f}C")
print(f"Maior:        {maior:.1f}C")
print(f"Menor:        {menor:.1f}C")
