# Capítulo 15 — Revisão: Tabela de conceitos em ação
# Um exemplo por conceito aprendido no livro

print("=== REVISÃO COMPLETA ===")
print()

# 1. Variáveis e tipos
nome = "Kelvin"
idade = 32
print(f"1. Variáveis: nome={nome}, idade={idade}")

# 2. Entrada (simulada para revisão)
# numero = int(input("Digite um número: "))
numero = 7  # valor fixo para demonstração
print(f"2. Entrada (simulada): numero={numero}")

# 3. Condição
if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"
print(f"3. Condição (IF): {numero} é {paridade}")

# 4. For
soma = 0
for i in range(1, numero + 1):
    soma += i
print(f"4. For: soma de 1 a {numero} = {soma}")

# 5. Lista
quadrados = [i ** 2 for i in range(1, 6)]  # versão avançada para o apêndice
print(f"5. Lista: quadrados de 1-5 = {quadrados}")

# 6. Função
def dobrar(valor):
    return valor * 2

print(f"6. Função: dobrar({numero}) = {dobrar(numero)}")

print()
print("Você domina esses 6 conceitos. Está pronto para o próximo nível.")
