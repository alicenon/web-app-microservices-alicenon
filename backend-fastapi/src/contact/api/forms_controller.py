# backend/api/forms_controller.py
from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any
from ..models.models import ContactForm
from ..use_cases.contact_use_case import process_contact_form
from pydantic import BaseModel

# import logging
# logger = logging.getLogger(__name__)

router = APIRouter(prefix="/contact", tags=["Contact Service"])


class SubmitResponse(BaseModel):
    message: str
    data: Dict[str, Any]

@router.post("/v1/submit",
            response_model=SubmitResponse,
            status_code=status.HTTP_201_CREATED)
async def submit_contact_form(form: ContactForm) -> SubmitResponse:
    """
    Endpoint para recibir y procesar el formulario de contacto.
    Este es el Controller que baso en Clean Architecture.
    """
    try:
        # Llama al caso de uso, pasándole los datos validados
        result = await process_contact_form(form)
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
