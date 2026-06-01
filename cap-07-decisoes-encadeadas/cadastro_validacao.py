# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 7 - Decisoes Encadeadas
# Snippet: validacao de formulario de cadastro - segundo exemplo
# ============================================================

# coleta os dados do formulario
nome = input("Nome completo: ")
email = input("E-mail: ")
senha = input("Senha (minimo 6 caracteres): ")

# verifica se TODOS os criterios sao atendidos ao mesmo tempo
nome_valido = len(nome) >= 3
email_valido = "@" in email
senha_valida = len(senha) >= 6

if nome_valido and email_valido and senha_valida:
    print("Cadastro realizado com sucesso.")

# identifica qual criterio falhou para dar feedback especifico
elif not nome_valido:
    print(f"Nome '{nome}' e muito curto. Use ao menos 3 caracteres.")
elif not email_valido:
    print(f"'{email}' nao parece um e-mail valido. Verifique o @.")
else:
    print("Senha fraca. Use ao menos 6 caracteres.")
