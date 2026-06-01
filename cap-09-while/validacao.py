# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 9 - While: Repetindo Ate Acontecer
# Snippet: validacao de numero positivo + jogo de adivinhar (exemplo central)
# ============================================================

# exemplo 1: pedir numero positivo ate o usuario digitar um valido
print("=== Validacao de numero positivo ===")
numero = 0  # valor inicial que garante a entrada no loop

while numero <= 0:
    entrada = input("Digite um numero positivo: ")
    numero = float(entrada)
    if numero <= 0:
        print("Esse valor nao e positivo. Tente novamente.")

print(f"Numero aceito: {numero}")

# exemplo 2: jogo de adivinhar (numero secreto = 42)
print("\n=== Jogo: Adivinhe o numero entre 1 e 100 ===")
numero_secreto = 42
tentativas = 0
acertou = False

while not acertou:
    chute = int(input("Seu chute: "))
    tentativas = tentativas + 1

    if chute < numero_secreto:
        print("Muito baixo. Tente um numero maior.")
    elif chute > numero_secreto:
        print("Muito alto. Tente um numero menor.")
    else:
        acertou = True  # muda a condicao - o loop vai encerrar
        print(f"Acertou em {tentativas} tentativa(s)!")
