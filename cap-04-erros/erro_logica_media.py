# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 4 - Erros Sao Parte do Processo
# Snippet: ilustracao de erro de logica - media com e sem parenteses
# ============================================================

# ERRO DE LOGICA: ordem de operacoes errada
nota_a = 8
nota_b = 6

# sem parenteses: Python calcula 6/2 primeiro, resultado e 11.0
media_errada = nota_a + nota_b / 2
print(f"Media incorreta: {media_errada}")

# CORRETO: parenteses forcam a adicao antes da divisao
media_correta = (nota_a + nota_b) / 2
print(f"Media correta: {media_correta}")

# ERRO DE EXECUCAO: o que acontece se o usuario nao digitar um numero
# descomente as linhas abaixo para ver o ValueError em acao
# numero = int(input("Digite um numero inteiro: "))
# print(f"Voce digitou: {numero}")
