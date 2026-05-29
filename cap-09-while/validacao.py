# Capítulo 9 — While: Repetindo até Acontecer
# Pede número positivo até o usuário digitar um válido

print("=== Validação de Entrada ===")

numero = -1  # valor inicial que força a entrada no loop

while numero <= 0:
    entrada = input("Digite um número positivo: ")
    numero = float(entrada)
    if numero <= 0:
        print("Número inválido. Tente novamente.")

print(f"Ótimo! Você digitou: {numero}")

print()

# Adivinhar número (bônus)
print("=== Jogo: Adivinhe o Número ===")
secreto = 42
tentativa = 0

while True:
    chute = int(input("Chute um número entre 1 e 100: "))
    tentativa += 1
    if chute < secreto:
        print("Muito baixo!")
    elif chute > secreto:
        print("Muito alto!")
    else:
        print(f"Acertou em {tentativa} tentativa(s)!")
        break
