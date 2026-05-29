# Exercícios Resolvidos — Todos os Capítulos
# Execute: python exercicios-resolvidos/todos_exercicios.py

print("=" * 50)
print("EXERCÍCIOS RESOLVIDOS — Lógica de Programação na Prática")
print("=" * 50)
print()

# -------------------------------------------------------------------
# CAP. 3 — Algoritmo: guarda-chuva (pseudocódigo executável)
# -------------------------------------------------------------------
print("--- Cap.3: Preciso de guarda-chuva? ---")
# Simplificado para rodar sem input
esta_chovendo = True
previsao_chuva = False

if esta_chovendo or previsao_chuva:
    print("Sim, leve o guarda-chuva.")
else:
    print("Não precisa de guarda-chuva.")
print()

# -------------------------------------------------------------------
# CAP. 5 — IMC
# -------------------------------------------------------------------
print("--- Cap.5: Calculadora de IMC ---")
peso = 70.0   # kg (fixo para teste)
altura = 1.75  # metros

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(f"Peso: {peso}kg, Altura: {altura}m")
print(f"IMC: {imc:.1f} — {categoria}")
print()

# -------------------------------------------------------------------
# CAP. 6 — Temperatura
# -------------------------------------------------------------------
print("--- Cap.6: Classificação de Temperatura ---")

def classificar_temperatura(temp):
    if temp < 15:
        return "fria"
    elif temp < 25:
        return "agradável"
    else:
        return "quente"

for temp_teste in [10, 20, 32]:
    print(f"{temp_teste}C: {classificar_temperatura(temp_teste)}")
print()

# -------------------------------------------------------------------
# CAP. 8 — Soma 1 a 100 (verificação com fórmula de Gauss)
# -------------------------------------------------------------------
print("--- Cap.8: Soma de 1 a 100 ---")
soma_loop = sum(range(1, 101))
soma_gauss = 100 * 101 // 2  # fórmula matemática para verificar
print(f"Soma com for:   {soma_loop}")
print(f"Fórmula Gauss:  {soma_gauss}")
print(f"Correto: {soma_loop == soma_gauss}")
print()

# -------------------------------------------------------------------
# CAP. 11 — Par ou ímpar (função)
# -------------------------------------------------------------------
print("--- Cap.11: Par ou Ímpar ---")

def eh_par(n):
    return n % 2 == 0

for num in [0, 1, 7, 42, 99, 100]:
    resultado = "par" if eh_par(num) else "ímpar"
    print(f"{num:3d}: {resultado}")
print()

# -------------------------------------------------------------------
# CAP. 14 — Ano bissexto (processo de 6 passos)
# -------------------------------------------------------------------
print("--- Cap.14: Ano Bissexto ---")

def eh_bissexto(ano):
    """
    Pseudocódigo:
      SE ano divisivel por 400: BISSEXTO
      SENÃO SE ano divisivel por 100: NÃO BISSEXTO
      SENÃO SE ano divisivel por 4: BISSEXTO
      SENÃO: NÃO BISSEXTO
    """
    return (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0)

# Testes (casos do Passo 2):
casos = [(2000, True), (1900, False), (2024, True), (2023, False), (2100, False)]
for ano, esperado in casos:
    resultado = eh_bissexto(ano)
    status = "OK" if resultado == esperado else "ERRO"
    print(f"{ano}: {'bissexto' if resultado else 'não bissexto'} [{status}]")
