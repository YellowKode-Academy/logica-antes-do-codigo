# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 13 - Lendo Erros como um Programador
# Snippet: exercicio resolvido - programa com 4 erros corrigidos
# ============================================================

# ERRO 1: IndexError - disciplinas[3] nao existe (indices validos: 0, 1, 2)
# ERRO 2: ZeroDivisionError - divisao por 0 em vez de len(notas)
# ERRO 3: SyntaxError - faltam os dois-pontos apos 'if media >= 7' e 'else'
# ERRO 4: NameError - 'resultado' nunca foi definido

# Codigo corrigido:
disciplinas = ["Matematica", "Portugues", "Historia"]
notas = [8.5, 7.0, 9.0]

print("Primeira disciplina:", disciplinas[0])
print("Terceira disciplina:", disciplinas[2])   # corrigido: indice valido

total = notas[0] + notas[1] + notas[2]
media = total / len(notas)                       # corrigido: dividir pela quantidade

if media >= 7:                                   # corrigido: dois-pontos
    situacao = "Aprovado"
else:                                            # corrigido: dois-pontos
    situacao = "Reprovado"

print("Media:", media)
print("Situacao:", situacao)
print("Resultado:", situacao)                    # corrigido: usar 'situacao'
