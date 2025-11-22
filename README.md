# Sistema de Gerenciamento - MongoDB

Sistema CRUD para gerenciamento de Usuários, Vendedores e Produtos usando MongoDB.

## 📋 Requisitos

- Python 3.13+
- MongoDB Atlas (ou MongoDB local)

## 🚀 Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
# Windows
.\.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install pymongo dnspython certifi
```

5. adiciona o mongo no aquivo`database.py`:
```env
uri = "bancoaqui"
```

## ▶️ Executar

```bash
python menu.py
```


## 📁 Estrutura

```
├── database.py          # Configuração MongoDB
├── menu.py             # Menu interativo
├── models/             # Modelos de dados
│   ├── usuario.py
│   ├── vendedor.py
│   └── produto.py
└── menus/              # Menus por módulo
    ├── usuarioMenu.py
    ├── vendedorMenu.py
    └── produtoMenu.py
```
