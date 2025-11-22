from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "bancoaqui"

client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadolivre

usuarios_colecao = db.usuario  
vendedores_colecao = db.vendedor  
print("ta conectadooo")
print(db.list_collection_names())  
