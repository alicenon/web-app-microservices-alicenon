from typing import Protocol
from ..models.models import ContactForm

class ContactRepository(Protocol):
    async def save_contact(self, contact: ContactForm) -> str:
        ...

class MongoContactRepository:
    def __init__(self, database, collection_name: str):
        self.db = database
        self.collection = self.db[collection_name] # Usar la coleccion especifica
        
    async def save_contact(self, contact: ContactForm) -> str:
        document = contact.model_dump()
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)
