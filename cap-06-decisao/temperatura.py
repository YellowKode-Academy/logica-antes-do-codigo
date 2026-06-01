# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 6 - Decisao: O IF que Voce Ja Usa Todo Dia
# Snippet: exercicio resolvido - classificacao de temperatura
# ============================================================

# recebe a temperatura do usuario
entrada = input("Digite a temperatura em graus Celsius: ")

# converte para numero decimal
temperatura = float(entrada)

# classifica a temperatura
if temperatura < 15:
    print(f"{temperatura}C - Temperatura fria.")
    print("Considere um casaco antes de sair.")
elif temperatura <= 24:
    print(f"{temperatura}C - Temperatura agradavel.")
    print("Bom dia para atividades ao ar livre.")
else:
    print(f"{temperatura}C - Temperatura quente.")
    print("Hidrate-se bem durante o dia.")
