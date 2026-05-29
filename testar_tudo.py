# testar_tudo.py — Testa toda a lógica do livro sem input() interativo
# Execute: python testar_tudo.py

erros = []
total = 0

def teste(nome, resultado, esperado):
    global total, erros
    total += 1
    ok = abs(resultado - esperado) < 0.001 if isinstance(esperado, float) else resultado == esperado
    status = "PASSOU" if ok else "ERRO"
    if not ok:
        erros.append(f"{nome}: esperado={esperado}, obtido={resultado}")
    print(f"  [{status}] {nome}")

print("=" * 50)
print("TESTES AUTOMATICOS — Logica de Programacao na Pratica")
print("=" * 50)

# --- CAP 4: Logica de media ---
print("\nCap 4 - Erro de logica (media):")
nota1, nota2 = 8, 6
media_errada = nota1 + nota2 / 2
media_correta = (nota1 + nota2) / 2
teste("media errada != correta", media_errada != media_correta, True)
teste("media correta = 7.0", media_correta, 7.0)

# --- CAP 5: Troco ---
print("\nCap 5 - Troco:")
def calcular_troco(preco, pagamento):
    return pagamento - preco

teste("troco R$50 pago R$100", calcular_troco(50, 100), 50.0)
teste("troco exato", calcular_troco(30, 30), 0.0)
teste("troco negativo (falta dinheiro)", calcular_troco(100, 80), -20.0)

# --- CAP 5: IMC ---
print("\nCap 5 - IMC:")
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

teste("IMC 70kg 1.75m = 22.9", round(calcular_imc(70, 1.75), 1), 22.9)
teste("IMC abaixo do peso", calcular_imc(50, 1.75) < 18.5, True)
teste("IMC sobrepeso", 25 <= calcular_imc(80, 1.70) < 30, True)

# --- CAP 6: Aprovacao ---
print("\nCap 6 - Aprovacao escolar:")
def classificar_nota(nota):
    if nota >= 7:   return "APROVADO"
    elif nota >= 5: return "RECUPERACAO"
    else:           return "REPROVADO"

teste("nota 8.5 = APROVADO", classificar_nota(8.5), "APROVADO")
teste("nota 6.0 = RECUPERACAO", classificar_nota(6.0), "RECUPERACAO")
teste("nota 3.0 = REPROVADO", classificar_nota(3.0), "REPROVADO")
teste("nota 7.0 = APROVADO", classificar_nota(7.0), "APROVADO")
teste("nota 5.0 = RECUPERACAO", classificar_nota(5.0), "RECUPERACAO")

# --- CAP 6: Temperatura ---
print("\nCap 6 - Temperatura:")
def classificar_temp(t):
    if t < 15:   return "fria"
    elif t < 25: return "agradavel"
    else:        return "quente"

teste("10C = fria",     classificar_temp(10), "fria")
teste("20C = agradavel",classificar_temp(20), "agradavel")
teste("32C = quente",   classificar_temp(32), "quente")

# --- CAP 8: FOR ---
print("\nCap 8 - For:")
soma_100 = sum(range(1, 101))
teste("soma 1 a 100 = 5050", soma_100, 5050)
teste("tabuada 7x5 = 35", 7 * 5, 35)

# --- CAP 11: Funcoes ---
print("\nCap 11 - Funcoes:")
def calcular_desconto(preco, percentual):
    return preco - preco * (percentual / 100)

def eh_par(n):
    return n % 2 == 0

def classificar_idade(idade):
    if idade < 12:   return "crianca"
    elif idade < 18: return "adolescente"
    elif idade < 60: return "adulto"
    else:            return "idoso"

teste("desconto 10% em R$100 = R$90", calcular_desconto(100, 10), 90.0)
teste("desconto 15% em R$200 = R$170", calcular_desconto(200, 15), 170.0)
teste("42 eh par", eh_par(42), True)
teste("7 eh impar", eh_par(7), False)
teste("5 anos = crianca", classificar_idade(5), "crianca")
teste("15 anos = adolescente", classificar_idade(15), "adolescente")
teste("30 anos = adulto", classificar_idade(30), "adulto")
teste("65 anos = idoso", classificar_idade(65), "idoso")

# --- CAP 12: Programa completo ---
print("\nCap 12 - Programa completo (media escolar):")
def calcular_media(notas):
    return sum(notas) / len(notas)

teste("media [8,7,9] = 8.0", calcular_media([8, 7, 9]), 8.0)
teste("media [5,5,5] = 5.0", calcular_media([5, 5, 5]), 5.0)
teste("media [3,4,2] = 3.0", calcular_media([3, 4, 2]), 3.0)

# --- CAP 14: Gorjeta ---
print("\nCap 14 - Calculadora de gorjeta:")
def calcular_gorjeta(conta, percentual):
    gorjeta = conta * (percentual / 100)
    return gorjeta, conta + gorjeta

g, t = calcular_gorjeta(100, 10)
teste("gorjeta R$100 + 10% = R$10", g, 10.0)
teste("total R$100 + 10% = R$110", t, 110.0)
g, t = calcular_gorjeta(85, 15)
teste("gorjeta R$85 + 15% = R$12.75", round(g, 2), 12.75)

# --- CAP 14: Ano bissexto ---
print("\nCap 14 - Ano bissexto:")
def eh_bissexto(ano):
    return (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0)

teste("2000 eh bissexto", eh_bissexto(2000), True)
teste("1900 nao eh bissexto", eh_bissexto(1900), False)
teste("2024 eh bissexto", eh_bissexto(2024), True)
teste("2023 nao eh bissexto", eh_bissexto(2023), False)
teste("2100 nao eh bissexto", eh_bissexto(2100), False)

# --- RESULTADO FINAL ---
print()
print("=" * 50)
passaram = total - len(erros)
print(f"RESULTADO: {passaram}/{total} testes passaram")
if erros:
    print("ERROS:")
    for e in erros:
        print(f"  - {e}")
else:
    print("Todos os testes passaram! Codigo pronto para o livro.")
print("=" * 50)
