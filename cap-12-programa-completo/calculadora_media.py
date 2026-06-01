# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 12 - Seu Primeiro Programa Completo
# Snippet: programa central - boletim com 3 trimestres
# ============================================================

def calcular_media(notas):
    # Soma todos os valores e divide pela quantidade
    return sum(notas) / len(notas)

def classificar_aluno(media):
    # Retorna a situacao com base nos criterios de aprovacao
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"

# Coleta as notas dos tres trimestres
notas = []
for trimestre in range(1, 4):
    nota = float(input(f"Nota do {trimestre}o trimestre: "))
    notas.append(nota)

# Calcula e classifica
media = calcular_media(notas)
situacao = classificar_aluno(media)

# Exibe o boletim completo
print("\n--- BOLETIM ---")
print(f"1o trimestre: {notas[0]:.1f}")
print(f"2o trimestre: {notas[1]:.1f}")
print(f"3o trimestre: {notas[2]:.1f}")
print(f"Media final:  {media:.1f}")
print(f"Situacao:     {situacao}")
