# backend/api/forms_controller.py
from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any

from ..infrastructure.database import get_database, get_contacts_collection_name
from ..infrastructure.contact_repository import MongoContactRepository
from ..models.models import ContactForm
from ..use_cases.contact_use_case import ContactUseCase
from pydantic import BaseModel

# import logging
# logger = logging.getLogger(__name__)

# router = APIRouter(prefix="/contact", tags=["Contact Service"])
router = APIRouter()


class SubmitResponse(BaseModel):
    message: str
    data: Dict[str, Any]

@router.post("/submit",
            response_model=SubmitResponse,
            status_code=status.HTTP_201_CREATED)
async def submit_contact_form(
    contact: ContactForm, 
    db=Depends(get_database), 
    collection_name: str = Depends(get_contacts_collection_name)
    ) -> SubmitResponse:
    """
    Endpoint para recibir y procesar el formulario de contacto.
    Este es el Controller que baso en Clean Architecture.
    """
    # Inyectar dependencias
    repository = MongoContactRepository(db, collection_name)
    use_case = ContactUseCase(repository)
    try:
        # Llama al caso de uso, pasándole los datos validados
        # result = await process_contact_form(form)
        result = await use_case.process_contact_form(contact)
        return SubmitResponse(
            message="Formulario recibido correctamente.",
            data=result)
    
    except Exception as e:
        # Manejo genérico de errores. En producción, loguea el error real.
        print(f"Error en el controller: {str(e)}") 
        raise HTTPException(
            status_code=500,
            detail="Ocurrió un error interno al procesar su solicitud."
        )
