# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 2
# Dia 10 - Listas e funcoes combinadas: nomes com mais de 5 letras, ordenados
# ============================================================

def filtrar_nomes_longos(nomes, min_letras=6):
    # retorna apenas os nomes com mais de 5 letras (default), em ordem alfabetica
    filtrados = [n for n in nomes if len(n) >= min_letras]
    filtrados.sort()
    return filtrados

# exemplo de uso
nomes = ["Ana", "Carlos", "Bia", "Fernanda", "Joao", "Beatriz", "Luiz", "Mariana"]
resultado = filtrar_nomes_longos(nomes)

print(f"Lista original: {nomes}")
print(f"Nomes com mais de 5 letras (ordem alfabetica): {resultado}")
