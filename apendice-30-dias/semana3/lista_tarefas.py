# ============================================================
# Livro: Logica de Programacao na Pratica
#        Do Pseudocodigo ao Python Real
# Autor: Kelvin Biffi
# Repo:  https://github.com/YellowKode-Academy/logica-antes-do-codigo
# Apendice - 30 Dias / Semana 3 - Mini-Projeto 2 (Dias 18 a 19)
# Snippet: lista de tarefas em memoria com adicionar/listar/concluir/remover
# ============================================================

# Lista de tarefas: cada item e um dicionario
# Exemplo: {"descricao": "Comprar leite", "concluida": False}
tarefas = []

def adicionar_tarefa(descricao):
    tarefas.append({"descricao": descricao, "concluida": False})

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    concluidas = sum(1 for t in tarefas if t["concluida"])
    print(f"\n{concluidas} de {len(tarefas)} tarefas concluidas:")
    for i, t in enumerate(tarefas, start=1):
        marca = "[X]" if t["concluida"] else "[ ]"
        print(f"{i}. {marca} {t['descricao']}")

def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
    else:
        print("Indice invalido.")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        print(f"Tarefa removida: {removida['descricao']}")
    else:
        print("Indice invalido.")

# Menu principal
while True:
    print("\n1-Adicionar  2-Listar  3-Concluir  4-Remover  0-Sair")
    opcao = input("Escolha: ")

    if opcao == "0":
        print("Encerrando.")
        break
    elif opcao == "1":
        desc = input("Descricao da tarefa: ")
        adicionar_tarefa(desc)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_tarefas()
        if tarefas:
            num = int(input("Numero da tarefa a concluir: "))
            marcar_concluida(num - 1)
    elif opcao == "4":
        listar_tarefas()
        if tarefas:
            num = int(input("Numero da tarefa a remover: "))
            remover_tarefa(num - 1)
    else:
        print("Opcao invalida.")
