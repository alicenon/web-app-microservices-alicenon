# instalamos el modulo para trabajar con mongodb.
# pip install motor
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["aspm-tool"]
users_collection = db["users"]
