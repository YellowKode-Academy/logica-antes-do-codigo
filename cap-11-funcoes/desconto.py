# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 11 - Funcoes: Reutilize o Raciocinio
# Snippet: tres funcoes - desconto, par e classificacao de idade
# ============================================================

# Tres funcoes independentes, cada uma com um proposito claro

def calcular_desconto(preco, percentual):
    # Calcula o preco final apos aplicar o desconto
    return preco - preco * percentual / 100

def eh_par(numero):
    # Retorna True se o numero for par, False se for impar
    return numero % 2 == 0

def classificar_idade(idade):
    # Retorna a categoria de acordo com a faixa etaria
    if idade < 12:
        return "crianca"
    elif idade < 18:
        return "adolescente"
    elif idade < 60:
        return "adulto"
    else:
        return "idoso"

# Chamando as funcoes com entradas diferentes
print(calcular_desconto(100, 10))   # 90.0
print(calcular_desconto(250, 15))   # 212.5
print(calcular_desconto(80, 5))     # 76.0

print(eh_par(4))    # True
print(eh_par(7))    # False

print(classificar_idade(8))    # crianca
print(classificar_idade(16))   # adolescente
print(classificar_idade(35))   # adulto
print(classificar_idade(65))   # idoso
