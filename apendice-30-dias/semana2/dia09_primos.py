# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 9 - Funcoes: eh_primo + listagem de primos entre 1 e 100
# ============================================================

def eh_primo(n):
    # 1 e numeros menores nao sao primos
    if n < 2:
        return False
    # verifica divisores de 2 ate n-1
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

# listar todos os primos entre 1 e 100
primos = []
for numero in range(1, 101):
    if eh_primo(numero):
        primos.append(numero)

print(f"Primos entre 1 e 100: {primos}")
print(f"Total: {len(primos)} primos.")
