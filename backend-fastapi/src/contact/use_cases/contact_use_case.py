# backend/use_cases/contact_use_case.py
from typing import Dict, Any
from ..models.models import ContactForm

# Simulamos una base de datos temporal. Reemplaza esto con tu conexión real.
fake_db = []


async def process_contact_form(form: ContactForm) -> Dict[str, Any]:
    """
    Caso de uso: Procesar el formulario de contacto.
    Esta es la capa Application en Clean Architecture.
    """
    # Aquí iría cualquier lógica adicional (validaciones de negocio, llamadas a servicios externos, etc.)

    # Convertimos el modelo a diccionario (los datos ya están sanitizados por Pydantic)
    form_data = form.model_dump()

    # Guardamos en "base de datos" (simulado)
    fake_db.append(form_data)

    # Aquí podrías llamar a un servicio de correo, logging, etc.
    print(f"[USE CASE] Formulario guardado: {form_data}")

    # Devolvemos información útil
    return {
        "id": len(fake_db),  # ID simulado
        "email": form_data["email"],
        "timestamp": "now"   # Timestamp real en el futuro
    }
