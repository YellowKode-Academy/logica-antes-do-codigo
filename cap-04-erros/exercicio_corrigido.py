# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 4 - Erros Sao Parte do Processo
# Snippet: exercicio resolvido - calculo de media corrigido
# ============================================================

# declarando as notas diretamente (sem input, para simplificar)
nota_prova = 7
nota_trabalho = 9

# calculando a media corretamente com parenteses
media = (nota_prova + nota_trabalho) / 2

# verificando aprovacao e exibindo resultado
if media >= 6:
    print(f"Aprovado com media {media:.1f}")
else:
    print(f"Reprovado com media {media:.1f}")
