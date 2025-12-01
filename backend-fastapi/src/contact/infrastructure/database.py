
from motor.motor_asyncio import AsyncIOMotorClient
#from src.core.config import settings # asi deberria ser con core y su env
# esta vez no usaré core/config.py porque aún no lo he aprendido bien
from typing import AsyncGenerator
import os
# Configuración de MongoDB
# MONGO_URI=mongodb://admin:alejandrols@localhost:27017
# MONGO_URL = os.getenv("MONGO_DETAILS", "mongodb://admin:alejandrols@localhost:27017")
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://admin:alejandrols@localhost:27017")
DB_NAME = "aspm-tool"
CONTACTS_COLLECTION_NAME = "contacts"
# Variables globales para la conexión   
mongo_client = None
mongo_db = None

async def connect_to_mongo():
    global mongo_client, mongo_db
    try:
        mongo_client = AsyncIOMotorClient(MONGODB_URL)
        mongo_db = mongo_client[DB_NAME]
        print("Conectado a MongoDB")
        print(f"Base de datos: {DB_NAME}")
        print(f"Colección: {CONTACTS_COLLECTION_NAME}")
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        raise
async def close_mongo_connection():
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("Conexión a MongoDB cerrada")
async def get_database():
    global mongo_db
    if mongo_db is None:
        raise Exception("La base de datos no está inizializada.")
    return mongo_db
# Para Inyectar el nombre de la colección
async def get_contacts_collection_name():
    return CONTACTS_COLLECTION_NAME