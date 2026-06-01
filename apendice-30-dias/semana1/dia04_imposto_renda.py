# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 1
# Dia 4 - Condicionais compostos: faixas de imposto de renda
# ============================================================

renda = float(input("Renda mensal (R$): "))

if renda <= 2000:
    aliquota = "Isento de IR"
elif renda <= 3000:
    aliquota = "7.5%"
elif renda <= 4500:
    aliquota = "15%"
else:
    aliquota = "22.5%"

print(f"Renda: R${renda:.2f}")
print(f"Aliquota: {aliquota}")
