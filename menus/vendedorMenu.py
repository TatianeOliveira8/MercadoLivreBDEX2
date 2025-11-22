from models import vendedor

def menu_vendedor():
    while True:
        print("\nMENU VENDEDOR")
        print("1 - Criar Vendedor")
        print("2 - Listar Vendedores")
        print("3 - Buscar Vendedor por ID")
        print("4 - Atualizar Vendedor")
        print("5 - Deletar Vendedor")
        print("S - Voltar")
        opcao = input("Escolha uma opção: ").upper()

        if opcao == "1":
            nome = input("Nome do vendedor: ")
            vid = vendedor.criar_vendedor(nome)
            print(f"Vendedor criado com ID: {vid}")

        elif opcao == "2":
            for v in vendedor.listar_vendedores():
                print(v)

        elif opcao == "3":
            vid = input("ID do vendedor: ")
            v = vendedor.ler_vendedor(vid)
            print(v if v else "Vendedor não encontrado")

        elif opcao == "4":
            vid = input("ID do vendedor: ")
            nome = input("Novo nome (Enter para pular): ") or None
            atualizado = vendedor.atualizar_vendedor(vid, nome)
            print("Atualizado!" if atualizado else "Nada a atualizar")

        elif opcao == "5":
            vid = input("ID do vendedor: ")
            deletado = vendedor.deletar_vendedor(vid)
            print("Deletado!" if deletado else "Vendedor não encontrado")

        elif opcao == "S":
            break
        else:
            print("Opção inválida!")
