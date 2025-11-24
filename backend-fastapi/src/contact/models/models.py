# backend/models/models.py
import html
from pydantic import BaseModel, EmailStr, field_validator


def sanitize(s: str) -> str:
    """Sanitiza una cadena contra XSS."""
    return html.escape(s.strip())


class ContactForm(BaseModel):
    nombre: str
    email: EmailStr
    mensaje: str

    @field_validator("nombre")
    def validate_name(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("El Nombre debe tener al menos 3 caracteres.")
        return sanitize(v)

    @field_validator("mensaje")
    def validate_message(cls, v):
        if len(v.strip()) < 5:
            raise ValueError("El Mensaje debe tener al menos 5 caracteres.")
        return sanitize(v)
