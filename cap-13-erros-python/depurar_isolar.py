# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 13 - Lendo Erros como um Programador
# Snippet: tecnica de depuracao - isolar e testar funcao com valores conhecidos
# ============================================================

# Em vez de tentar entender 50 linhas de uma vez,
# comente tudo e va descomentando bloco por bloco
notas = [8.5, 7.0]
# media = calcular_media(notas)   # descomente e veja se quebra
# situacao = classificar_aluno(media)
print(notas)  # comeca pelo mais simples e avanca


# Testando a funcao isoladamente com entrada controlada
def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

resultado = calcular_media([8.0, 7.0, 9.0])
print(resultado)  # esperado: 8.0 - se der diferente, o bug esta na funcao
