from menus.usuarioMenu import menu_usuario
from menus.vendedorMenu import menu_vendedor
from menus.produtoMenu import menu_produto

def menu_principal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1 - CRUD Usuário")
        print("2 - CRUD Vendedor")
        print("3 - CRUD Produto")
        print("S - Sair")
        opcao = input("Digite a opção desejada: ").upper()

        if opcao == "1":
            menu_usuario()
        elif opcao == "2":
            menu_vendedor()
        elif opcao == "3":
            menu_produto()
        elif opcao == "S":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu_principal()