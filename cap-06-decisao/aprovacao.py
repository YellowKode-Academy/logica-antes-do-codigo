# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 6 - Decisao: O IF que Voce Ja Usa Todo Dia
# Snippet: aprovacao escolar com if/elif/else
# ============================================================

# solicita a nota ao usuario
nota_texto = input("Digite a nota do aluno (0 a 10): ")

# converte para numero decimal
nota = float(nota_texto)

# verifica se a nota e valida
if nota < 0 or nota > 10:
    print("Nota invalida. Digite um valor entre 0 e 10.")

# verifica aprovacao direta
elif nota >= 7:
    print("Situacao: APROVADO")
    print(f"Nota final: {nota}")

# verifica se vai para recuperacao
elif nota >= 5:
    print("Situacao: RECUPERACAO")
    print(f"Nota final: {nota}")
    print(f"Precisa tirar {14 - nota:.1f} pontos na recuperacao para passar.")

# reprovado abaixo de 5
else:
    print("Situacao: REPROVADO")
    print(f"Nota final: {nota}")
