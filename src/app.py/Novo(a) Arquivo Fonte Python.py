from src.controllers.tarefa_controller import (
    adicionar_tarefa,
    listar_tarefas,
    marcar_concluida
)
from src.views.interface import mostrar_tarefas
from src.services.foco_service import calcular_tempo_total
from src.services.salvar import salvar_dados


def menu():
    print("\n===== FOCUS TRACK =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Tempo total")
    print("5. Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            
            try:
                tempo = int(input("Tempo (em minutos): "))
                adicionar_tarefa(nome, tempo)
                print("✅ Tarefa adicionada!")
            except ValueError:
                print("❌ Digite um número válido para o tempo.")

        elif opcao == "2":
            tarefas = listar_tarefas()
            if tarefas:
                mostrar_tarefas(tarefas)
            else:
                print("⚠️ Nenhuma tarefa cadastrada.")

        elif opcao == "3":
            tarefas = listar_tarefas()
            mostrar_tarefas(tarefas)

            try:
                indice = int(input("Número da tarefa para concluir: ")) - 1
                marcar_concluida(indice)
                print("✅ Tarefa concluída!")
            except:
                print("❌ Entrada inválida.")

        elif opcao == "4":
            tarefas = listar_tarefas()
            total = calcular_tempo_total(tarefas)
            print(f"⏱️ Tempo total: {total} minutos")

        elif opcao == "5":
            salvar_dados(listar_tarefas())
            print("💾 Dados salvos. Saindo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()