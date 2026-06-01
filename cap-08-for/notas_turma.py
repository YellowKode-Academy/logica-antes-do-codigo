# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 8 - Repeticao: Fazendo o Computador Trabalhar por Voce
# Snippet: segundo exemplo - media e maior nota de uma turma com 4 alunos
# ============================================================

# numero de alunos definido no inicio
quantidade_alunos = 4

# acumuladores e variavel de controle
soma_notas = 0
maior_nota = 0  # comeca no menor valor possivel para notas

print(f"Digite as notas dos {quantidade_alunos} alunos:")

# percorre os alunos de 1 ate quantidade_alunos
for aluno in range(1, quantidade_alunos + 1):
    entrada = input(f"Nota do aluno {aluno}: ")
    nota = float(entrada)

    # acumula a soma
    soma_notas = soma_notas + nota

    # atualiza o maior se a nota atual for maior
    if nota > maior_nota:
        maior_nota = nota

# calcula a media apos o loop
media = soma_notas / quantidade_alunos

print(f"\nSoma total: {soma_notas}")
print(f"Media da turma: {media:.2f}")
print(f"Maior nota: {maior_nota}")
