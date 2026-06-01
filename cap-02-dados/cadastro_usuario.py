# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 2 - Dados Sao Informacao
# Snippet: cadastro com input - exercicio resolvido (formulario)
# ============================================================

# recebendo os tres campos do formulario via input
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

# exibindo a mensagem de boas-vindas personalizada com f-string
print(f"Ola, {nome}!")
print(f"Voce tem {idade} anos e mora em {cidade}.")
print("Bem-vindo ao sistema.")
