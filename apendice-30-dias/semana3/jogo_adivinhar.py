# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 3 - Mini-Projeto 1 (Dias 15 a 17)
# Snippet: jogo de adivinhar com placar e opcao de jogar de novo
# ============================================================

import random

def sortear_numero(minimo, maximo):
    return random.randint(minimo, maximo)

def verificar_palpite(palpite, numero_secreto):
    if palpite < numero_secreto:
        return "baixo"
    elif palpite > numero_secreto:
        return "alto"
    else:
        return "correto"

def jogar_uma_partida(tentativas_maximas=7):
    numero_secreto = sortear_numero(1, 100)
    tentativas = 0
    print(f"\nAdivinhe o numero entre 1 e 100. Voce tem {tentativas_maximas} tentativas.")

    while tentativas < tentativas_maximas:
        palpite = int(input("Seu palpite: "))
        tentativas += 1
        resultado = verificar_palpite(palpite, numero_secreto)

        if resultado == "correto":
            print(f"Acertou em {tentativas} tentativa(s)!")
            return True
        elif resultado == "baixo":
            print(f"Muito baixo. Restam {tentativas_maximas - tentativas} tentativa(s).")
        else:
            print(f"Muito alto. Restam {tentativas_maximas - tentativas} tentativa(s).")

    print(f"Suas tentativas acabaram. O numero era {numero_secreto}.")
    return False

# Placar de partidas
vitorias = 0
derrotas = 0

while True:
    venceu = jogar_uma_partida()
    if venceu:
        vitorias += 1
    else:
        derrotas += 1

    print(f"Placar -> Vitorias: {vitorias} | Derrotas: {derrotas}")
    resposta = input("Jogar de novo? (s/n): ")
    if resposta.lower() != "s":
        print("Ate a proxima!")
        break
