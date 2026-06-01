# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 11 - Funcoes: Reutilize o Raciocinio
# Snippet: exercicio resolvido - calcular_imc e classificar_imc encadeadas
# ============================================================

def calcular_imc(peso, altura):
    # IMC = peso dividido pelo quadrado da altura
    return peso / (altura ** 2)

def classificar_imc(imc):
    # Retorna a categoria de acordo com a OMS
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidade"

# Integrando as duas funcoes
peso = 75
altura = 1.75

imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

print(f"IMC: {imc:.1f}")        # IMC: 24.5
print(f"Categoria: {categoria}") # Categoria: peso normal
