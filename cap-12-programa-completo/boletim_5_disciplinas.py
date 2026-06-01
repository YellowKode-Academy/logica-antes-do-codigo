# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 12 - Seu Primeiro Programa Completo
# Snippet: exercicio resolvido - boletim com 5 disciplinas + maior/menor
# ============================================================

# --- parte 1: coleta de dados ---

def calcular_media(notas):
    # Media simples: soma dividida pela quantidade
    return sum(notas) / len(notas)

def classificar_aluno(media):
    # Criterios de aprovacao
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"

# Coleta disciplinas e notas
disciplinas = []
notas = []

for i in range(1, 6):
    nome = input(f"Nome da disciplina {i}: ")
    nota = float(input(f"Nota de {nome}: "))
    disciplinas.append(nome)
    notas.append(nota)

# --- parte 2: processamento e resultado ---

# Calcula resultados
media = calcular_media(notas)
situacao = classificar_aluno(media)
indice_maior = notas.index(max(notas))
indice_menor = notas.index(min(notas))

# Exibe o boletim
print("\n--- BOLETIM FINAL ---")
for i in range(len(disciplinas)):
    print(f"{disciplinas[i]}: {notas[i]:.1f}")

print(f"\nMedia geral:  {media:.1f}")
print(f"Situacao:     {situacao}")
print(f"Maior nota:   {notas[indice_maior]:.1f} ({disciplinas[indice_maior]})")
print(f"Menor nota:   {notas[indice_menor]:.1f} ({disciplinas[indice_menor]})")
