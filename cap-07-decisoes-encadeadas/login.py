# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 7 - Decisoes Encadeadas
# Snippet: exercicio resolvido - sistema de login com 3 tentativas
# ============================================================

# credenciais validas (em sistemas reais, nunca ficam no codigo assim)
usuario_valido = "admin"
senha_valida = "1234"

# contador de tentativas
tentativas = 0
limite = 3

# loop de tentativas - explicado em detalhe no proximo capitulo
while tentativas < limite:
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    tentativas = tentativas + 1

    # verifica se usuario E senha estao corretos ao mesmo tempo
    if usuario == usuario_valido and senha == senha_valida:
        print("Acesso liberado. Bem-vindo!")
        break  # sai do loop ao acertar

    else:
        restantes = limite - tentativas
        if restantes > 0:
            print(f"Credenciais incorretas. {restantes} tentativa(s) restante(s).")
        else:
            print("Conta bloqueada por excesso de tentativas.")
