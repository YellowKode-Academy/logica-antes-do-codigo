# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 5 - Sequencia: A Base de Tudo
# Snippet: exercicio resolvido - calculadora de IMC com classificacao
# ============================================================

# == ENTRADA ==
# recebendo peso e altura do usuario e convertendo para float
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# == PROCESSAMENTO ==
# calculando o IMC: peso dividido pelo quadrado da altura
imc = peso / (altura ** 2)

# classificando o resultado conforme as faixas padronizadas
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Peso normal"
elif imc < 30.0:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# == SAIDA ==
# exibindo IMC com uma casa decimal e a classificacao
print(f"Seu IMC e: {imc:.1f}")
print(f"Classificacao: {classificacao}")
