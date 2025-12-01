# backend/use_cases/contact_use_case.py
from datetime import datetime
from typing import Dict, Any

from ..infrastructure.contact_repository import ContactRepository
from ..models.models import ContactForm

class ContactUseCase:
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    async def process_contact_form(self, form: ContactForm) -> Dict[str, Any]:
        """
        Caso de uso: Procesar el formulario de contacto.
        Esta es la capa Application en Clean Architecture.
        """
        # Aquí iría cualquier lógica adicional (validaciones de negocio, llamadas a servicios externos, etc.)

        # Convertimos el modelo a diccionario (los datos ya están sanitizados por Pydantic)
        form_data = form.model_dump()

        # Guardamos en MongoDB usando el repositorio
        contact_id = await self.repository.save_contact(form)

        # Aquí podrías llamar a un servicio de correo, logging, etc.
        print(f"[USE CASE] Formulario guardado: {form_data}")

        # Devolvemos información útil
        return {
            "id": contact_id,  # ID real de MongoDB
            "email": form_data["email"],
            "timestamp": datetime.now().isoformat()  # Timestamp real
        }
