import os, sys
sys.path.append('..')

from database import usuarios_colecao
from models.produto import ler_produto, reduzir_estoque
import uuid
from datetime import datetime


# ===========================================
#                CRUD USUÁRIO
# ===========================================

def criar_usuario(nome, email, telefone, endereco):
    usuario_id = str(uuid.uuid4())
    usuario = {
        "usuario_id": usuario_id,
        "nome_usuario": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco,
        "compras": [],
        "favoritos": []
    }
    usuarios_colecao.insert_one(usuario)
    print(f"Usuário {nome} criado com sucesso!")
    return usuario_id


def ler_usuario(usuario_id):
    usuario = usuarios_colecao.find_one({"usuario_id": usuario_id})
    if usuario:
        return usuario
    print("Usuário não encontrado.")
    return None


def listar_usuarios():
    return list(usuarios_colecao.find())


def atualizar_usuario(usuario_id, nome=None, email=None, telefone=None, endereco=None):
    update = {}
    if nome: update["nome_usuario"] = nome
    if email: update["email"] = email
    if telefone: update["telefone"] = telefone
    if endereco: update["endereco"] = endereco

    if not update:
        print("Nenhum dado para atualizar.")
        return False

    usuarios_colecao.update_one({"usuario_id": usuario_id}, {"$set": update})
    print("Usuário atualizado com sucesso!")
    return True


def deletar_usuario(usuario_id):
    result = usuarios_colecao.delete_one({"usuario_id": usuario_id})
    if result.deleted_count:
        print("Usuário deletado com sucesso!")
        return True

    print("Usuário não encontrado.")
    return False


# ===========================================
#                 COMPRAS
# ===========================================

def adicionar_compra(usuario_id, itens_info):
    """
    itens_info -> [{"produto_id": "...", "quantidade": X}, ...]
    """

    # Agrupa caso o usuário repita o mesmo produto
    agregado = {}
    for item in itens_info:
        pid = item.get("produto_id")
        quantidade = int(item.get("quantidade", 0))
        if pid and quantidade > 0:
            agregado[pid] = agregado.get(pid, 0) + quantidade

    if not agregado:
        print("Nenhum item válido informado.")
        return None

    itens = []
    valor_total = 0.0

    # Primeiro valida todo estoque antes de debitar
    for pid, quantidade in agregado.items():
        produto = ler_produto(pid)

        if not produto:
            print(f"Produto {pid} não existe. Compra cancelada.")
            return None

        estoque = produto.get("estoque", 0)
        if estoque < quantidade:
            print(f"Estoque insuficiente para {produto['nome_produto']}. Disponível: {estoque}")
            print("Compra cancelada.")
            return None

    # Agora sim debita estoque e monta compra
    for pid, quantidade in agregado.items():
        produto = ler_produto(pid)

        preco = float(produto.get("preco_produto"))
        nome = produto.get("nome_produto")

        subtotal = preco * quantidade
        valor_total += subtotal

        itens.append({
            "produto_id": pid,
            "nome_produto": nome,
            "preco_unitario": preco,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

        # reduz estoque no banco
        reduzir_estoque(pid, quantidade)

    compra = {
        "compra_id": str(uuid.uuid4()),
        "data_compra": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "valor_total": round(valor_total, 2),
        "itens": itens
    }

    usuarios_colecao.update_one(
        {"usuario_id": usuario_id},
        {"$push": {"compras": compra}}
    )

    print(f"Compra adicionada com sucesso! Total R${valor_total:.2f}")
    return compra["compra_id"]


# ===========================================
#                 FAVORITOS
# ===========================================

def adicionar_favorito(usuario_id, produto_id):
    if not ler_produto(produto_id):
        print("Produto não existe. Não é possível favoritar.")
        return False

    usuarios_colecao.update_one(
        {"usuario_id": usuario_id},
        {"$addToSet": {"favoritos": produto_id}}
    )
    print("Favorito adicionado!")
    return True


def listar_favoritos(usuario_id):
    usuario = ler_usuario(usuario_id)
    if usuario:
        return usuario.get("favoritos", [])
    return []


def remover_favorito(usuario_id, produto_id):
    usuarios_colecao.update_one(
        {"usuario_id": usuario_id},
        {"$pull": {"favoritos": produto_id}}
    )
    print("Favorito removido!")
    return True
