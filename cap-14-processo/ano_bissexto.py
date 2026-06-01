# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 14 - Do Pseudocodigo ao Python: O Processo de 6 Passos
# Snippet: exercicio resolvido - verificador de ano bissexto com asserts
# ============================================================

# Passo 1: o que entra? Um ano inteiro.
# O que sai? True (bissexto) ou False (nao bissexto).
# Regra: divisivel por 4, exceto se divisivel por 100,
#         exceto se divisivel por 400.

# Passo 2: exemplos concretos
# 2000 -> True  (divisivel por 400)
# 1900 -> False (divisivel por 100, mas nao por 400)
# 2024 -> True  (divisivel por 4, nao por 100)
# 2023 -> False (nao divisivel por 4)

# Passo 3: pseudocodigo
# SE ano % 400 == 0: RETORNAR Verdadeiro
# SENAO SE ano % 100 == 0: RETORNAR Falso
# SENAO SE ano % 4 == 0: RETORNAR Verdadeiro
# SENAO: RETORNAR Falso

# Passo 4: estruturas - funcao com if/elif/else, operador %

def eh_bissexto(ano):
    # Passo 5: traducao direta do pseudocodigo
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

# Modo interativo
ano = int(input("Digite um ano: "))
if eh_bissexto(ano):
    print(f"{ano} e um ano bissexto.")
else:
    print(f"{ano} nao e um ano bissexto.")

# Passo 6: testes com os exemplos do Passo 2
print("\n--- Verificando com exemplos conhecidos ---")
assert eh_bissexto(2000) == True,  "2000 falhou - deveria ser bissexto"
assert eh_bissexto(1900) == False, "1900 falhou - nao deveria ser bissexto"
assert eh_bissexto(2024) == True,  "2024 falhou - deveria ser bissexto"
assert eh_bissexto(2023) == False, "2023 falhou - nao deveria ser bissexto"
print("Todos os testes passaram.")
