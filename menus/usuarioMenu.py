from models import usuario

def menu_usuario():
    while True:
        print("\nMENU USUÁRIO")
        print("1 - Criar Usuário")
        print("2 - Listar Usuários")
        print("3 - Buscar Usuário por ID")
        print("4 - Atualizar Usuário")
        print("5 - Deletar Usuário")
        print("6 - Adicionar Compra")
        print("7 - Adicionar Favorito")
        print("8 - Remover Favorito")
        print("9 - Listar Favoritos")
        print("S - Voltar")

        opcao = input("Escolha uma opção: ").upper()

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            user_id = usuario.criar_usuario(nome, email, telefone, endereco)
            print(f"Usuário criado com ID: {user_id}")

        elif opcao == "2":
            for u in usuario.listar_usuarios():
                print(u)

        elif opcao == "3":
            uid = input("ID do usuário: ")
            u = usuario.ler_usuario(uid)
            print(u if u else "Usuário não encontrado")

        elif opcao == "4":
            uid = input("ID: ")
            nome = input("Novo nome (Enter p/ pular): ") or None
            email = input("Novo email (Enter p/ pular): ") or None
            telefone = input("Novo telefone (Enter p/ pular): ") or None
            endereco = input("Novo endereço (Enter p/ pular): ") or None
            usuario.atualizar_usuario(uid, nome, email, telefone, endereco)

        elif opcao == "5":
            uid = input("ID do usuário: ")
            usuario.deletar_usuario(uid)

        elif opcao == "6":
            uid = input("ID do usuário: ")

            itens_info = []
            print("\nAdicione os produtos da compra. Aperte Enter no ID para terminar.")

            while True:
                pid = input("ID do produto: ").strip()
                if pid == "":
                    break

                quantidade = int(input("Quantidade: "))
                itens_info.append({"produto_id": pid, "quantidade": quantidade})

            usuario.adicionar_compra(uid, itens_info)

        elif opcao == "7":
            uid = input("ID do usuário: ")
            pid = input("ID do produto favorito: ")
            usuario.adicionar_favorito(uid, pid)

        elif opcao == "8":
            uid = input("ID do usuário: ")
            pid = input("ID do produto a remover: ")
            usuario.remover_favorito(uid, pid)

        elif opcao == "9":
            uid = input("ID do usuário: ")
            favs = usuario.listar_favoritos(uid)
            print(favs if favs else "Nenhum favorito")

        elif opcao == "S":
            break

        else:
            print("Opção inválida")
