# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 12 - Seu Primeiro Programa Completo
# ============================================================
# Calculadora de média escolar com 3 disciplinas

def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)

def classificar_aluno(media):
    """Retorna a situação do aluno baseada na média."""
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def coletar_notas(disciplinas):
    """Coleta as notas do usuário para cada disciplina."""
    notas = []
    for disciplina in disciplinas:
        nota = float(input(f"Nota em {disciplina}: "))
        notas.append(nota)
    return notas


# Programa principal
print("=== Boletim Escolar ===")
print()

disciplinas = ["Matemática", "Português", "Ciências"]
notas = coletar_notas(disciplinas)

media = calcular_media(notas)
situacao = classificar_aluno(media)

print()
print("--- RESULTADO ---")
for i, disciplina in enumerate(disciplinas):
    print(f"{disciplina}: {notas[i]:.1f}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
