from models import vendedor
from models.produto import criar_produto, ler_produto, atualizar_produto, deletar_produto

def menu_produto():
    while True:
        print("\nMENU PRODUTO")
        print("1 - Listar todos os produtos")
        print("2 - Adicionar produto a um vendedor")
        print("3 - Atualizar produto")
        print("4 - Remover produto")
        print("S - Voltar")
        opcao = input("Escolha uma opção: ").upper()

        if opcao == "1":
            for vend in vendedor.listar_vendedores():
                print(f"\nVendedor: {vend['nome_vendedor']} (ID: {vend['vendedor_id']})")
                for prod in vend.get("produtos", []):
                    print(f"  ID: {prod['produto_id']}, Nome: {prod['nome_produto']}, "
                          f"Preço: {prod['preco_produto']}, Estoque: {prod['estoque']}, "
                          f"Ativo: {prod['ativo']}")

        elif opcao == "2":
            vid = input("ID do vendedor: ")
            v = vendedor.ler_vendedor(vid)
            if not v:
                print("Vendedor não encontrado!")
                continue

            nome = input("Nome do produto: ")
            desc = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque inicial: "))
            ativo = input("Produto ativo? (s/n): ").strip().lower() == "s"

            pid = criar_produto(nome, desc, preco, vid)
            atualizar_produto(pid, estoque=estoque, ativo=ativo)
            print(f"Produto adicionado com ID: {pid}")

        elif opcao == "3":
            pid = input("ID do produto: ")
            prod = ler_produto(pid)
            if not prod:
                print("Produto não encontrado!")
                continue

            nome = input("Novo nome (Enter para pular): ") or None
            desc = input("Nova descrição (Enter para pular): ") or None
            preco_input = input("Novo preço (Enter para pular): ")
            preco = float(preco_input) if preco_input else None
            estoque_input = input("Novo estoque (Enter para pular): ")
            estoque = int(estoque_input) if estoque_input else None
            ativo_input = input("Ativo? (s/n ou Enter para pular): ").strip().lower()
            ativo = True if ativo_input == "s" else False if ativo_input == "n" else None

            atualizar_produto(pid, nome, desc, preco, estoque, ativo)
            print("Produto atualizado com sucesso!")

        elif opcao == "4":
            pid = input("ID do produto: ")
            prod = ler_produto(pid)
            if not prod:
                print("Produto não encontrado!")
                continue
            deletar_produto(pid)
            print("Produto removido com sucesso!")

        elif opcao == "S":
            break
        else:
            print("Opção inválida, tente novamente.")
