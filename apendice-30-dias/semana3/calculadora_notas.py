# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 3 - Mini-Projeto 3 (Dias 20 a 21)
# Snippet: calculadora de medias com ranking e medalhas
# ============================================================

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"

# Coleta de dados
alunos = []  # cada item: {"nome": str, "notas": list, "media": float}

quantidade = int(input("Quantos alunos? "))
for _ in range(quantidade):
    nome = input("Nome do aluno: ")
    notas = []
    for n in range(1, 4):
        nota = float(input(f"Nota {n} de {nome}: "))
        notas.append(nota)
    media = calcular_media(notas)
    alunos.append({"nome": nome, "notas": notas, "media": media})

# Ordenacao por media (maior primeiro)
alunos.sort(key=lambda a: a["media"], reverse=True)

# Exibe ranking com medalhas para os 3 primeiros
medalhas = ["1o", "2o", "3o"]
print("\n--- RANKING ---")
for posicao, aluno in enumerate(alunos, start=1):
    if posicao <= 3:
        marca = medalhas[posicao - 1]
    else:
        marca = f"{posicao}o"
    situacao = classificar(aluno["media"])
    print(f"{marca} {aluno['nome']} - Media: {aluno['media']:.1f} ({situacao})")
