# Capítulo 7 — Decisões Encadeadas: Sistema de Login
# Demonstra AND, OR e condições compostas

USUARIO_CORRETO = "kelvin"
SENHA_CORRETA = "python123"
MAX_TENTATIVAS = 3

print("=== Sistema de Login ===")

tentativas = 0
acesso = False

while tentativas < MAX_TENTATIVAS:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    # Condição composta: ambos precisam estar corretos
    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        acesso = True
        break
    else:
        tentativas += 1
        restantes = MAX_TENTATIVAS - tentativas
        if restantes > 0:
            print(f"Credenciais inválidas. {restantes} tentativa(s) restante(s).")
        else:
            print("Conta bloqueada por excesso de tentativas.")

if acesso:
    print(f"Bem-vindo, {usuario}! Acesso liberado.")
