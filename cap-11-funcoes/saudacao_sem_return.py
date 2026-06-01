# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 11 - Funcoes: Reutilize o Raciocinio
# Snippet: funcao sem return retorna None (demonstracao)
# ============================================================

def saudacao(nome):
    print(f"Ola, {nome}!")
    # sem return

resultado = saudacao("Ana")
print(resultado)  # None - a funcao nao devolveu nada
