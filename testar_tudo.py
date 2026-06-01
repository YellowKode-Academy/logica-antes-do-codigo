# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# testar_tudo.py - Suite de testes para todas as funcoes do livro
# Execute: python testar_tudo.py
# ============================================================
# Texto plano, sem caracteres especiais que quebram cp1252 no Windows.

erros = []
total = 0


def teste(nome, resultado, esperado):
    global total, erros
    total += 1
    if isinstance(esperado, float) and isinstance(resultado, (int, float)):
        ok = abs(resultado - esperado) < 0.001
    else:
        ok = resultado == esperado
    status = "PASSOU" if ok else "ERRO  "
    if not ok:
        erros.append(f"{nome}: esperado={esperado}, obtido={resultado}")
    print(f"  [{status}] {nome}")


print("=" * 60)
print("TESTES AUTOMATICOS - Logica de Programacao na Pratica")
print("=" * 60)

# --- CAP 4: Erro de logica - media ---
print("\nCap 4 - Erro de logica (media):")
nota1, nota2 = 8, 6
media_errada = nota1 + nota2 / 2
media_correta = (nota1 + nota2) / 2
teste("media errada != correta", media_errada != media_correta, True)
teste("media correta = 7.0", media_correta, 7.0)
teste("media errada = 11.0", media_errada, 11.0)


# --- CAP 5: Troco ---
print("\nCap 5 - Troco:")

def calcular_troco(preco, pagamento):
    return pagamento - preco

teste("troco R$50 pago R$100", calcular_troco(50, 100), 50.0)
teste("troco exato", calcular_troco(30, 30), 0.0)
teste("troco negativo (falta dinheiro)", calcular_troco(100, 80), -20.0)
teste("troco grande", calcular_troco(15.70, 20.00), 4.3)


# --- CAP 5: IMC ---
print("\nCap 5 - IMC:")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

teste("IMC 70kg 1.75m = 22.9", round(calcular_imc(70, 1.75), 1), 22.9)
teste("IMC abaixo do peso", calcular_imc(50, 1.75) < 18.5, True)
teste("IMC sobrepeso", 25 <= calcular_imc(80, 1.70) < 30, True)
teste("IMC obesidade", calcular_imc(120, 1.70) >= 30, True)


# --- CAP 6: Aprovacao escolar ---
print("\nCap 6 - Aprovacao escolar:")

def classificar_nota(nota):
    if nota >= 7:   return "APROVADO"
    elif nota >= 5: return "RECUPERACAO"
    else:           return "REPROVADO"

teste("nota 8.5 = APROVADO", classificar_nota(8.5), "APROVADO")
teste("nota 6.0 = RECUPERACAO", classificar_nota(6.0), "RECUPERACAO")
teste("nota 3.0 = REPROVADO", classificar_nota(3.0), "REPROVADO")
teste("nota 7.0 = APROVADO (limite)", classificar_nota(7.0), "APROVADO")
teste("nota 5.0 = RECUPERACAO (limite)", classificar_nota(5.0), "RECUPERACAO")
teste("nota 4.9 = REPROVADO", classificar_nota(4.9), "REPROVADO")


# --- CAP 6: Temperatura ---
print("\nCap 6 - Temperatura:")

def classificar_temp(t):
    if t < 15:   return "fria"
    elif t <= 24: return "agradavel"
    else:        return "quente"

teste("10C = fria",      classificar_temp(10), "fria")
teste("20C = agradavel", classificar_temp(20), "agradavel")
teste("24C = agradavel (limite)", classificar_temp(24), "agradavel")
teste("32C = quente",    classificar_temp(32), "quente")


# --- CAP 6: Velocidade ---
print("\nCap 6 - Velocidade:")

def classificar_velocidade(v):
    if v < 60:    return "baixa"
    elif v <= 80: return "regular"
    elif v <= 100: return "leve excesso"
    else:         return "excesso grave"

teste("50 km/h = baixa", classificar_velocidade(50), "baixa")
teste("70 km/h = regular", classificar_velocidade(70), "regular")
teste("90 km/h = leve excesso", classificar_velocidade(90), "leve excesso")
teste("120 km/h = excesso grave", classificar_velocidade(120), "excesso grave")


# --- CAP 7: Desconto fidelidade ---
print("\nCap 7 - Desconto fidelidade:")

def calcular_desconto_cliente(anos, valor):
    if anos > 1 and valor > 100:
        return valor * 0.15
    elif anos <= 1 and valor > 200:
        return valor * 0.05
    return 0.0

teste("cliente 2 anos R$200 = R$30 desconto", calcular_desconto_cliente(2, 200), 30.0)
teste("cliente 1 ano R$250 = R$12.50 desconto", calcular_desconto_cliente(1, 250), 12.5)
teste("cliente 3 anos R$50 = sem desconto", calcular_desconto_cliente(3, 50), 0.0)


# --- CAP 7: Validacao de cadastro ---
print("\nCap 7 - Validacao de cadastro:")

def validar_cadastro(nome, email, senha):
    return len(nome) >= 3 and "@" in email and len(senha) >= 6

teste("cadastro valido", validar_cadastro("Ana", "a@b.com", "secret"), True)
teste("nome curto", validar_cadastro("Jo", "j@b.com", "secret"), False)
teste("email sem @", validar_cadastro("Joao", "joaobcom", "secret"), False)
teste("senha curta", validar_cadastro("Joao", "j@b.com", "abc"), False)


# --- CAP 8: FOR e acumulador ---
print("\nCap 8 - For e acumulador:")
soma_100 = sum(range(1, 101))
teste("soma 1 a 100 = 5050", soma_100, 5050)
teste("tabuada 7x5 = 35", 7 * 5, 35)
teste("range(1,11) tem 10 numeros", len(list(range(1, 11))), 10)


# --- CAP 9: Validacao de numero positivo ---
print("\nCap 9 - Validacao:")

def numero_no_intervalo(n, minimo, maximo):
    return minimo <= n <= maximo

teste("5 entre 1 e 10", numero_no_intervalo(5, 1, 10), True)
teste("-1 fora", numero_no_intervalo(-1, 1, 10), False)
teste("11 fora", numero_no_intervalo(11, 1, 10), False)
teste("1 dentro (limite)", numero_no_intervalo(1, 1, 10), True)
teste("10 dentro (limite)", numero_no_intervalo(10, 1, 10), True)


# --- CAP 9: Caixa registradora ---
print("\nCap 9 - Caixa:")

def somar_itens(valores):
    # soma itens parando ao encontrar 0
    total = 0
    for v in valores:
        if v == 0:
            break
        total += v
    return total

teste("itens [10, 20, 30, 0] = 60", somar_itens([10, 20, 30, 0]), 60)
teste("lista vazia = 0", somar_itens([0]), 0)


# --- CAP 10: Listas ---
print("\nCap 10 - Listas:")
notas = [8.5, 7.0, 9.2, 6.8, 10.0]
teste("sum(notas)", sum(notas), 41.5)
teste("len(notas) = 5", len(notas), 5)
teste("max(notas) = 10.0", max(notas), 10.0)
teste("min(notas) = 6.8", min(notas), 6.8)
teste("media notas = 8.3", round(sum(notas) / len(notas), 1), 8.3)


# --- CAP 10: Filtrar temperaturas ---
print("\nCap 10 - Filtrar temperaturas:")

def filtrar_frias(temps, limite=20):
    return [t for t in temps if t < limite]

teste("frias [18.5, 32.0, 25.3, 14.8] = [18.5, 14.8]",
      filtrar_frias([18.5, 32.0, 25.3, 14.8]), [18.5, 14.8])
teste("sem frias", filtrar_frias([30, 40, 50]), [])


# --- CAP 11: Funcoes desconto, par, idade ---
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
teste("desconto 5% em R$80 = R$76", calcular_desconto(80, 5), 76.0)
teste("42 eh par", eh_par(42), True)
teste("7 eh impar", eh_par(7), False)
teste("0 eh par", eh_par(0), True)
teste("5 anos = crianca", classificar_idade(5), "crianca")
teste("15 anos = adolescente", classificar_idade(15), "adolescente")
teste("30 anos = adulto", classificar_idade(30), "adulto")
teste("65 anos = idoso", classificar_idade(65), "idoso")
teste("12 anos = adolescente (limite)", classificar_idade(12), "adolescente")
teste("60 anos = idoso (limite)", classificar_idade(60), "idoso")


# --- CAP 11: IMC com funcao + classificacao ---
print("\nCap 11 - IMC com classificacao:")

def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidade"

teste("IMC 16 = abaixo do peso", classificar_imc(16), "abaixo do peso")
teste("IMC 22 = peso normal", classificar_imc(22), "peso normal")
teste("IMC 27 = sobrepeso", classificar_imc(27), "sobrepeso")
teste("IMC 32 = obesidade", classificar_imc(32), "obesidade")


# --- CAP 12: Programa completo (media escolar) ---
print("\nCap 12 - Programa completo (media escolar):")

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_aluno(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"

teste("media [8,7,9] = 8.0", calcular_media([8, 7, 9]), 8.0)
teste("media [5,5,5] = 5.0", calcular_media([5, 5, 5]), 5.0)
teste("media [3,4,2] = 3.0", calcular_media([3, 4, 2]), 3.0)
teste("classificar 8.0 = Aprovado", classificar_aluno(8.0), "Aprovado")
teste("classificar 5.5 = Recuperacao", classificar_aluno(5.5), "Recuperacao")
teste("classificar 4.0 = Reprovado", classificar_aluno(4.0), "Reprovado")


# --- CAP 14: Calculadora de gorjeta ---
print("\nCap 14 - Calculadora de gorjeta:")

def calcular_gorjeta(conta, percentual):
    gorjeta = conta * (percentual / 100)
    return gorjeta, conta + gorjeta

g, t = calcular_gorjeta(80, 10)
teste("gorjeta R$80 + 10% = R$8", g, 8.0)
teste("total R$80 + 10% = R$88", t, 88.0)
g, t = calcular_gorjeta(150, 15)
teste("gorjeta R$150 + 15% = R$22.50", round(g, 2), 22.5)
teste("total R$150 + 15% = R$172.50", round(t, 2), 172.5)
g, t = calcular_gorjeta(200, 20)
teste("gorjeta R$200 + 20% = R$40", g, 40.0)
teste("total R$200 + 20% = R$240", t, 240.0)


# --- CAP 14: Ano bissexto ---
print("\nCap 14 - Ano bissexto:")

def eh_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

teste("2000 eh bissexto", eh_bissexto(2000), True)
teste("1900 nao eh bissexto", eh_bissexto(1900), False)
teste("2024 eh bissexto", eh_bissexto(2024), True)
teste("2023 nao eh bissexto", eh_bissexto(2023), False)
teste("2100 nao eh bissexto", eh_bissexto(2100), False)
teste("1600 eh bissexto", eh_bissexto(1600), True)


# --- APENDICE: FizzBuzz ---
print("\nApendice Dia 7 - FizzBuzz:")

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

teste("fizzbuzz(15) = FizzBuzz", fizzbuzz(15), "FizzBuzz")
teste("fizzbuzz(9) = Fizz", fizzbuzz(9), "Fizz")
teste("fizzbuzz(10) = Buzz", fizzbuzz(10), "Buzz")
teste("fizzbuzz(7) = '7'", fizzbuzz(7), "7")
teste("fizzbuzz(30) = FizzBuzz", fizzbuzz(30), "FizzBuzz")


# --- APENDICE: Imposto de renda ---
print("\nApendice Dia 4 - Imposto de renda:")

def aliquota_ir(renda):
    if renda <= 2000:
        return "Isento de IR"
    elif renda <= 3000:
        return "7.5%"
    elif renda <= 4500:
        return "15%"
    else:
        return "22.5%"

teste("R$1500 = Isento", aliquota_ir(1500), "Isento de IR")
teste("R$2500 = 7.5%", aliquota_ir(2500), "7.5%")
teste("R$4000 = 15%", aliquota_ir(4000), "15%")
teste("R$6000 = 22.5%", aliquota_ir(6000), "22.5%")


# --- APENDICE: Numero primo ---
print("\nApendice Dia 9 - Numero primo:")

def eh_primo(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

teste("2 eh primo", eh_primo(2), True)
teste("7 eh primo", eh_primo(7), True)
teste("9 nao eh primo", eh_primo(9), False)
teste("1 nao eh primo", eh_primo(1), False)
teste("97 eh primo", eh_primo(97), True)


# --- APENDICE: Filtro de nomes longos ---
print("\nApendice Dia 10 - Filtro de nomes:")

def filtrar_nomes_longos(nomes, min_letras=6):
    filtrados = [n for n in nomes if len(n) >= min_letras]
    filtrados.sort()
    return filtrados

teste("filtrar nomes >= 6 letras",
      filtrar_nomes_longos(["Ana", "Carlos", "Bia", "Fernanda"]),
      ["Carlos", "Fernanda"])
teste("lista vazia retorna vazia", filtrar_nomes_longos([]), [])


# --- APENDICE: Contar vogais ---
print("\nApendice Dia 11 - Vogais:")

def contar_vogais(texto):
    return sum(1 for c in texto if c in "aeiouAEIOU")

teste("contar vogais 'banana'", contar_vogais("banana"), 3)
teste("contar vogais 'Ola Mundo'", contar_vogais("Ola Mundo"), 4)
teste("contar vogais frase vazia", contar_vogais(""), 0)


# --- APENDICE: Conversor de temperatura ---
print("\nApendice Dia 14 - Conversor de medidas:")

def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

teste("0C = 32F", celsius_para_fahrenheit(0), 32.0)
teste("100C = 212F", celsius_para_fahrenheit(100), 212.0)
teste("32F = 0C", fahrenheit_para_celsius(32), 0.0)
teste("212F = 100C", fahrenheit_para_celsius(212), 100.0)


# --- APENDICE Dia 16: Verificar palpite ---
print("\nApendice Dia 16 - Verificar palpite:")

def verificar_palpite(palpite, secreto):
    if palpite < secreto:
        return "baixo"
    elif palpite > secreto:
        return "alto"
    else:
        return "correto"

teste("palpite 30, secreto 42 = baixo", verificar_palpite(30, 42), "baixo")
teste("palpite 50, secreto 42 = alto", verificar_palpite(50, 42), "alto")
teste("palpite 42, secreto 42 = correto", verificar_palpite(42, 42), "correto")


# --- RESULTADO FINAL ---
print()
print("=" * 60)
passaram = total - len(erros)
print(f"RESULTADO: {passaram}/{total} testes passaram")
if erros:
    print("\nERROS:")
    for e in erros:
        print(f"  - {e}")
else:
    print("Todos os testes passaram. Codigo do livro validado.")
print("=" * 60)
