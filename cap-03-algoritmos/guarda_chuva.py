# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 3 - Algoritmos Ja Existem na Sua Vida
# Snippet: exercicio resolvido - decidir se leva guarda-chuva (operador or)
# ============================================================

# recebendo as condicoes climaticas do usuario
chovendo_agora = input("Esta chovendo agora? (s/n): ")
probabilidade_chuva = int(input("Probabilidade de chuva prevista (0 a 100): "))

# verificando se alguma das condicoes indica necessidade de guarda-chuva
if chovendo_agora == "s" or probabilidade_chuva > 70:
    print("Leve o guarda-chuva.")
else:
    print("Nao precisa de guarda-chuva hoje.")
