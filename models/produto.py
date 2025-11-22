from database import vendedores_colecao
import uuid

def criar_produto(nome, descricao_produto, preco_produto, vendedor_id):
    produto_id = str(uuid.uuid4())
    produto = {
        "produto_id": produto_id,
        "nome_produto": nome,
        "descricao_produto": descricao_produto,
        "preco_produto": preco_produto,
        "estoque": 0,
        "ativo": True
    }
    vendedores_colecao.update_one(
        {"vendedor_id": vendedor_id},
        {"$push": {"produtos": produto}}
    )
    print(f"Produto {nome} criado com sucesso no vendedor {vendedor_id}!")
    return produto_id

def ler_produto(produto_id):
    vendedor = vendedores_colecao.find_one(
        {"produtos.produto_id": produto_id},
        {"produtos.$": 1}
    )
    if vendedor and "produtos" in vendedor:
        return vendedor["produtos"][0]

    print("Produto não encontrado.")
    return None


def atualizar_produto(produto_id, nome=None, descricao_produto=None, preco_produto=None, estoque=None, ativo=None):
    update = {}

    if nome: update["produtos.$.nome_produto"] = nome
    if descricao_produto: update["produtos.$.descricao_produto"] = descricao_produto
    if preco_produto is not None: update["produtos.$.preco_produto"] = preco_produto
    if estoque is not None: update["produtos.$.estoque"] = estoque
    if ativo is not None: update["produtos.$.ativo"] = ativo

    if not update:
        print("Nenhum dado fornecido para atualização.")
        return

    vendedores_colecao.update_one(
        {"produtos.produto_id": produto_id},
        {"$set": update}
    )

def deletar_produto(produto_id):
    vendedores_colecao.update_one(
        {"produtos.produto_id": produto_id},
        {"$pull": {"produtos": {"produto_id": produto_id}}}
    )

def reduzir_estoque(produto_id, quantidade):
    produto = ler_produto(produto_id)
    if not produto:
        print("Produto não existe.")
        return False

    estoque_atual = produto["estoque"]

    if estoque_atual < quantidade:
        print(f"Estoque insuficiente. Disponível: {estoque_atual}")
        return False

    novo_estoque = estoque_atual - quantidade

    vendedores_colecao.update_one(
        {"produtos.produto_id": produto_id},
        {"$set": {"produtos.$.estoque": novo_estoque}}
    )
    return True
