# Capítulo 2 — Dados São Informação
# Variáveis são caixinhas com etiqueta. Tipos definem o que cabe dentro.

# Tipos básicos de dados
nome = "Kelvin"           # texto (string)
idade = 32                # número inteiro (int)
altura = 1.78             # número decimal (float)
programador = True        # verdadeiro ou falso (bool)

print("=== Tipos de Dados ===")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É programador?", programador)

print()

# Entrada do usuário
print("=== Cadastro Simples ===")
nome_usuario = input("Digite seu nome: ")
cidade = input("Cidade: ")
print(f"Olá, {nome_usuario} de {cidade}!")
