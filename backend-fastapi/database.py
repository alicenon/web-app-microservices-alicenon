# instalamos el modulo para trabajar con mongo.
# pip install motor
'''
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Usa una URI por defecto si no hay variable de entorno
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client.hestia_db  # Nombre de la base de datos
'''

from motor.motor_asyncio import AsyncIOMotorClient

#CONN A MONGODB LOCAL (DOCKER)
client = AsyncIOMotorClient("mongodb://admin:alejandrols@localhost:27017")
db = client["aspm-tool"] # base de datos
users_collection = db["users"] # Coleccion de usuarios