# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 4 - Modulos da Biblioteca Padrao
# Snippet: import datetime - data atual, formatacao e diferenca de datas
# ============================================================

import datetime

hoje = datetime.date.today()
print(hoje)                          # ex: 2026-05-29

agora = datetime.datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))  # ex: 29/05/2026 14:30

nascimento = datetime.date(1990, 3, 15)
diferenca = hoje - nascimento
print(f"Dias vividos desde 1990-03-15: {diferenca.days}")
