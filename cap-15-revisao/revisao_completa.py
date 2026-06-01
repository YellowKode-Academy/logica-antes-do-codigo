# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 15 - O Que Voce Aprendeu - e o Que Vem a Seguir
# Snippet: programa que usa todos os 8 conceitos do livro
# ============================================================

# Revisao: variaveis, tipos, sequencia, if/elif/else,
# for, while, listas e funcoes - tudo em um programa so

def classificar_nota(nota):
    # Funcao com if/elif/else - Conceito 8 + 4
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"

# Variaveis e tipos - Conceitos 1 e 2
disciplinas = []  # lista vazia - Conceito 7
notas = []

# Loop while para coleta - Conceito 6
continuar = True
while continuar:
    nome = input("Nome da disciplina (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        continuar = False
    else:
        nota = float(input(f"Nota de {nome}: "))
        disciplinas.append(nome)
        notas.append(nota)

# Sequencia de processamento - Conceito 3
# Loop for para exibir resultados - Conceito 5
print("\n--- BOLETIM FINAL ---")
for i in range(len(disciplinas)):
    classificacao = classificar_nota(notas[i])
    print(f"{disciplinas[i]}: {notas[i]:.1f} ({classificacao})")
