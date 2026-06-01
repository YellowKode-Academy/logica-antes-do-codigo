# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 11 - Strings e listas: contar palavras, vogais e palavra mais longa
# ============================================================

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    total = 0
    for c in texto:
        if c in vogais:
            total += 1
    return total

def palavra_mais_longa(palavras):
    mais_longa = ""
    for p in palavras:
        if len(p) > len(mais_longa):
            mais_longa = p
    return mais_longa

frase = input("Digite uma frase: ")

palavras = frase.split()
total_palavras = len(palavras)
total_vogais = contar_vogais(frase)
maior_palavra = palavra_mais_longa(palavras)

print(f"Total de palavras: {total_palavras}")
print(f"Total de vogais:   {total_vogais}")
print(f"Palavra mais longa: '{maior_palavra}' ({len(maior_palavra)} letras)")
