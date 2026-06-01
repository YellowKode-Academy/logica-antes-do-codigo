# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 6 - Decisao: O IF que Voce Ja Usa Todo Dia
# Snippet: segundo exemplo - classificacao de velocidade em via de 80 km/h
# ============================================================

# recebe a velocidade do usuario
entrada = input("Digite a velocidade atual (km/h): ")
velocidade = float(entrada)

# classifica a velocidade em relacao ao limite de 80 km/h
if velocidade < 60:
    print(f"{velocidade} km/h - Velocidade baixa. Possivel lentidao no transito.")
elif velocidade <= 80:
    # chegou aqui: ja sabemos que velocidade >= 60
    print(f"{velocidade} km/h - Velocidade regular. Dentro do limite.")
elif velocidade <= 100:
    # chegou aqui: ja sabemos que velocidade > 80
    print(f"{velocidade} km/h - Atencao: leve excesso de velocidade.")
else:
    # chegou aqui: velocidade > 100
    print(f"{velocidade} km/h - Excesso grave. Multa automatica registrada.")
