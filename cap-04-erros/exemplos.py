# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 4 - Erros Sao Parte do Processo
# ============================================================
# Três tipos de erro: Sintaxe, Lógica, Execução
# Este arquivo mostra exemplos CORRETOS com comentários sobre os erros comuns

# ERRO DE LÓGICA (o código roda mas o resultado está errado)
print("=== Erro de Lógica ===")

# Calcular média — versão ERRADA (erro de lógica)
nota1 = 8
nota2 = 6
media_errada = nota1 + nota2 / 2   # ← erro: divisão tem precedência, divide só nota2
print(f"Média errada: {media_errada}")   # resultado: 11.0 (errado!)

# Calcular média — versão CORRETA
media_correta = (nota1 + nota2) / 2     # parênteses garantem a soma primeiro
print(f"Média correta: {media_correta}")  # resultado: 7.0 (correto!)

print()

# COMO LER UMA MENSAGEM DE ERRO
print("=== Anatomia de um Erro ===")
print("Quando Python mostra um erro, leia de baixo para cima:")
print("  1. Última linha: o TIPO do erro (SyntaxError, NameError...)")
print("  2. Penúltima linha: a DESCRIÇÃO do erro")
print("  3. Linha acima: em qual LINHA do seu código está o problema")
