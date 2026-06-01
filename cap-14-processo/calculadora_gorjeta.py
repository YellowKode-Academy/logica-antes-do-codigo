# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 14 - Do Pseudocodigo ao Python: O Processo de 6 Passos
# Snippet: programa central - calculadora de gorjeta com asserts
# ============================================================

# Passo 1: entender o problema - conta + percentual -> gorjeta e total
# Passo 3: pseudocodigo foi escrito antes deste codigo

def calcular_gorjeta(conta, percentual):
    # Passo 5: traducao direta do pseudocodigo para Python
    gorjeta = conta * percentual / 100
    total = conta + gorjeta
    return gorjeta, total  # Python permite retornar dois valores

# Modo interativo: pede os dados ao usuario
conta = float(input("Valor da conta (R$): "))
percentual = float(input("Percentual de gorjeta (%): "))

gorjeta, total = calcular_gorjeta(conta, percentual)

print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")
print(f"Total da conta:   R$ {total:.2f}")

# Passo 6: testes automaticos com os exemplos do Passo 2
print("\n--- Verificando com exemplos conhecidos ---")
assert calcular_gorjeta(80, 10) == (8.0, 88.0), "Caso 1 falhou"
assert calcular_gorjeta(150, 15) == (22.5, 172.5), "Caso 2 falhou"
assert calcular_gorjeta(200, 20) == (40.0, 240.0), "Caso 3 falhou"
print("Todos os testes passaram.")
