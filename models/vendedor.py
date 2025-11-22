import os, sys
sys.path.append('..')

from database import vendedores_colecao
import uuid
from models.produto import criar_produto as criar_produto_arquivo
from models.produto import atualizar_produto as atualizar_produto_arquivo
from models.produto import deletar_produto as deletar_produto_arquivo
from models.produto import ler_produto as ler_produto_arquivo

def criar_vendedor(nome_vendedor):
    vendedor_id = str(uuid.uuid4())
    vendedor = {
        "vendedor_id": vendedor_id,
        "nome_vendedor": nome_vendedor,
        "produtos": []      
    }
    vendedores_colecao.insert_one(vendedor)
    print(f"Vendedor {nome_vendedor} criado com sucesso!")
    return vendedor_id

def ler_vendedor(vendedor_id):
    vendedor = vendedores_colecao.find_one({"vendedor_id": vendedor_id})
    if vendedor:
        return vendedor
    print("Vendedor não encontrado.")
    return None

def listar_vendedores():
    return list(vendedores_colecao.find())

def atualizar_vendedor(vendedor_id, nome_vendedor=None):
    update = {}
    if nome_vendedor:
        update["nome_vendedor"] = nome_vendedor

    if update:
        vendedores_colecao.update_one({"vendedor_id": vendedor_id}, {"$set": update})
        print("Vendedor atualizado com sucesso!")
        return True
    else:
        print("Nenhum dado para atualizar.")
        return False

def deletar_vendedor(vendedor_id):
    result = vendedores_colecao.delete_one({"vendedor_id": vendedor_id})
    if result.deleted_count:
        print("Vendedor deletado com sucesso!")
        return True
    else:
        return False

def adicionar_produto(vendedor_id, nome_produto, descricao_produto, preco_produto):
    return criar_produto_arquivo(nome_produto, descricao_produto, preco_produto, vendedor_id)

def atualizar_produto_vendedor(produto_id, nome=None, descricao_produto=None, preco_produto=None, estoque=None, ativo=None):
    return atualizar_produto_arquivo(produto_id, nome, descricao_produto, preco_produto, estoque, ativo)
def remover_produto_vendedor(produto_id):
    return deletar_produto_arquivo(produto_id)
def ler_produto_vendedor(produto_id):
    return ler_produto_arquivo(produto_id)
