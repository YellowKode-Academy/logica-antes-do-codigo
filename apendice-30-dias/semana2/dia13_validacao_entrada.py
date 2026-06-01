# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 13 - Validacao de entrada sem travar o programa
# ============================================================

def ler_numero(mensagem):
    while True:
        entrada = input(mensagem)
        # remove um possivel ponto para validar inteiros e decimais
        teste = entrada.replace('.', '', 1).replace('-', '', 1)
        if teste.isnumeric():
            return float(entrada)
        print("Entrada invalida, tente novamente.")

numero = ler_numero("Digite um numero: ")
print(f"Numero valido recebido: {numero}")
