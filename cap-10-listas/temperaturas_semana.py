# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 10 - Listas: Guardando Varios Valores
# Snippet: segundo exemplo - filtrar dias quentes/frios com listas paralelas
# ============================================================

# lista de temperaturas registradas ao longo de uma semana (graus Celsius)
temperaturas = [18.5, 32.0, 25.3, 14.8, 30.1, 22.7, 11.2]
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

# listas separadas para guardar dias frios e quentes
dias_frios = []
dias_quentes = []

# percorre as temperaturas com seus indices
for i in range(len(temperaturas)):
    temp = temperaturas[i]
    dia = dias[i]

    if temp < 20:
        dias_frios.append(dia)
    else:
        dias_quentes.append(dia)

# exibe o resultado
print(f"Dias frios (abaixo de 20C): {dias_frios}")
print(f"Dias quentes (20C ou mais): {dias_quentes}")

# calcula a media da semana
media = sum(temperaturas) / len(temperaturas)
print(f"Temperatura media da semana: {media:.1f}C")
