# backend/models/models.py
import html
from pydantic import BaseModel, EmailStr, field_validator

# Función para sanitizar entradas y prevenir XSS
#ataques XSS (Cross-Site Scripting) en el frontend o al renderizar HTML
def sanitize(s: str) -> str:
    """Sanitiza una cadena contra XSS."""
    return html.escape(s.strip())


class ContactForm(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str

    @field_validator("nombre")
    def validate_name(cls, v):
        # Validar que el nombre tenga al menos 3 caracteres y maximo 100   
        if len(v.strip()) < 3:
            raise ValueError("El Nombre debe tener al menos 3 caracteres.")
        if len(v.strip()) > 100:
            raise ValueError("El Nombre no debe exceder 100 caracteres.")
        return sanitize(v)

    @field_validator("mensaje")
    def validate_message(cls, v):
        if len(v.strip()) < 5:
            raise ValueError("El Mensaje debe tener al menos 5 caracteres.")
        if len(v.strip()) > 1000:
            raise ValueError("El Mensaje no debe exceder 1000 caracteres.")
        return sanitize(v)
