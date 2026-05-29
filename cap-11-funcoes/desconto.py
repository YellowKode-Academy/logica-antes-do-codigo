# Capítulo 11 — Funções: Reutilize o Raciocínio

def calcular_desconto(preco, percentual):
    """Calcula o preço final após aplicar desconto percentual."""
    valor_desconto = preco * (percentual / 100)
    preco_final = preco - valor_desconto
    return preco_final

def eh_par(numero):
    """Retorna True se o número for par, False se for ímpar."""
    return numero % 2 == 0

def classificar_idade(idade):
    """Classifica a pessoa por faixa etária."""
    if idade < 12:
        return "criança"
    elif idade < 18:
        return "adolescente"
    elif idade < 60:
        return "adulto"
    else:
        return "idoso"


# Testando as funções
print("=== Calculadora de Desconto ===")
preco = float(input("Preço original (R$): "))
desconto = float(input("Percentual de desconto (%): "))
final = calcular_desconto(preco, desconto)
print(f"Preço com {desconto}% de desconto: R${final:.2f}")

print()
print("=== Par ou Ímpar ===")
n = int(input("Digite um número: "))
if eh_par(n):
    print(f"{n} é PAR")
else:
    print(f"{n} é ÍMPAR")

print()
print("=== Classificação por Idade ===")
idade = int(input("Sua idade: "))
print(f"Classificação: {classificar_idade(idade)}")
