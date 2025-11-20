# backend/models.py
import html
from pydantic import BaseModel, EmailStr , field_validator
# FastAPI por defecto protege de muchas amenazas...
'''
Validación de datos con Pydantic
 - Rechaza cualquier petición si falta un campo/tipo de dato
 - Validación email con formato correcto (EmailStr).
'''
#Sanitización -> limpia datos antes de guardar.
def limpiar(s: str) -> str:
    return html.escape(s.strip())
class ContactForm(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str
# pip install email-validator
    @field_validator("nombre")
    def validar_nombre(cls, v):
        if len(v.strip()) < 3:
            # para nombres cortos como: Ana, Leo o Eva
            print("El nombre debe tener al menos 3 caracteres.")
            raise ValueError("El Nombre debe tener al menos 3 caracteres.")
        
        return limpiar(v)
    
    @field_validator("mensaje")
    def validar_mensaje(cls, v):
        if len(v.strip()) < 5:
            # para mensajes cortos... 
            print("El Mensaje debe tener al menos 5 caracteres.")
            raise ValueError("El Mensaje debe tener al menos 5 caracteres.")
        
        return limpiar(v)
        

