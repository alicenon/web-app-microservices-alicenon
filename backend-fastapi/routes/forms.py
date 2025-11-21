from fastapi import APIRouter, HTTPException
from models.models import ContactForm

router = APIRouter(prefix="/forms", tags=["forms"])

@router.post("/")
async def crear_formulario(form: ContactForm):
    try:
        datos = ""
        datos = str(form.dict())
        print(" -> " + datos)
        # Con un Async tenemos a la espera un await
        # Aquí guardamos/insertar en MongoDB
        # await db...
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar: {str(e)}")