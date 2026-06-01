# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 6 - Decisao: O IF que Voce Ja Usa
# ============================================================
#
# Pseudocódigo:
#   RECEBER nota
#   SE nota >= 7
#       MOSTRAR "Aprovado"
#   SENÃO SE nota >= 5
#       MOSTRAR "Recuperação"
#   SENÃO
#       MOSTRAR "Reprovado"

print("=== Sistema de Aprovação ===")

nota = float(input("Digite a nota (0 a 10): "))

# Validação da entrada
if nota < 0 or nota > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
elif nota >= 7:
    print(f"Nota: {nota} — APROVADO ✓")
elif nota >= 5:
    print(f"Nota: {nota} — RECUPERAÇÃO")
else:
    print(f"Nota: {nota} — REPROVADO")
