# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 13 - Lendo Erros como um Programador
# ============================================================
# Exemplos de erros comuns e como interpretá-los

print("=== Tipos de Erro em Python ===")
print()

# 1. NameError — variável não existe
print("--- NameError ---")
print("Causa: usar uma variável antes de criá-la")
print("Código problemático: print(resultado)  # resultado não foi definido")
print("Solução: definir a variável antes de usar")
resultado = 42
print(f"Correto: resultado = 42, depois print(resultado) → {resultado}")
print()

# 2. TypeError — tipo errado
print("--- TypeError ---")
print("Causa: operação com tipos incompatíveis")
numero = "5"  # string, não int
# numero + 3  ← isso geraria TypeError: can only concatenate str (not "int") to str
numero_int = int(numero)  # converter antes
print(f"Correto: int('5') + 3 = {numero_int + 3}")
print()

# 3. ZeroDivisionError — divisão por zero
print("--- ZeroDivisionError ---")
print("Causa: tentar dividir por zero")
divisor = int(input("Digite um divisor (tente 0): "))
if divisor == 0:
    print("Erro: não é possível dividir por zero!")
else:
    print(f"100 / {divisor} = {100 / divisor:.2f}")
print()

# 4. IndexError — índice fora do alcance
print("--- IndexError ---")
frutas = ["maçã", "banana", "laranja"]
print(f"Lista: {frutas}")
print(f"Índices válidos: 0, 1, 2 (total: {len(frutas)} itens)")
indice = int(input("Digite um índice para acessar: "))
if 0 <= indice < len(frutas):
    print(f"frutas[{indice}] = {frutas[indice]}")
else:
    print(f"IndexError! Índice {indice} está fora do intervalo 0-{len(frutas)-1}")
