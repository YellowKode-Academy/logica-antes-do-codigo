# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Capitulo 13 - Lendo Erros como um Programador
# Snippet: agregado de versoes corrigidas dos 6 erros comuns
# ============================================================
# Cada secao mostra um erro tipico e a versao corrigida.
# Os trechos com erro estao COMENTADOS para o arquivo rodar sem crashar.

print("=== Tipos de Erro em Python (versoes corrigidas) ===\n")

# 1. SyntaxError - gramatica errada (so ilustrativo - codigo errado nao roda)
print("--- SyntaxError ---")
print("Codigo ERRADO (comentado): if nota >= 7  <- falta os dois-pontos")
# Versao CORRETA: dois-pontos sao obrigatorios apos if, else, for, while, def
nota = 8.5
if nota >= 7:
    print(f"Aprovado: {nota}")
print()

# 2. NameError - variavel nao definida
print("--- NameError ---")
print("Codigo ERRADO (comentado): print(resultado) antes de definir 'resultado'")
# Versao CORRETA: definir antes de usar
nota1 = 8.0
nota2 = 7.5
media = (nota1 + nota2) / 2
print(f"Media: {media}")  # 7.75
print()

# 3. TypeError - tipos incompativeis
print("--- TypeError ---")
print("Codigo ERRADO (comentado): 2026 - input(...) - subtrair int de string")
# Versao CORRETA: converter input para int antes de operar
idade_texto = "25"  # simulando entrada do usuario
idade = int(idade_texto)
ano_nascimento = 2026 - idade
print(f"Voce nasceu em {ano_nascimento}")
print()

# 4. ZeroDivisionError - divisao por zero
print("--- ZeroDivisionError ---")
print("Codigo ERRADO (comentado): sum([]) / len([]) - len de lista vazia e 0")
# Versao CORRETA: verificar se a lista tem elementos antes de dividir
notas = []
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Media: {media}")
else:
    print("Nenhuma nota registrada.")
print()

# 5. IndexError - indice fora do alcance
print("--- IndexError ---")
print("Codigo ERRADO (comentado): frutas[5] em uma lista de 3 itens")
# Versao CORRETA: acessar apenas indices que existem
frutas = ["maca", "banana", "laranja"]
if len(frutas) > 5:
    print(frutas[5])
else:
    print(f"A lista tem apenas {len(frutas)} elementos.")
print()

# 6. ValueError - conversao impossivel
print("--- ValueError ---")
print("Codigo ERRADO (comentado): int('vinte') - texto nao numerico")
# Versao CORRETA: verificar se a entrada pode ser convertida antes
entrada = "25"  # simulando entrada valida
if entrada.isdigit():
    idade = int(entrada)
    print(f"Voce tem {idade} anos.")
else:
    print("Entrada invalida. Digite apenas numeros.")
