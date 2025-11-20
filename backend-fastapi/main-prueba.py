# ejemplo de usar el contact de React
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Configuración CORS para permitir peticiones desde React (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)
'''
Para Prod...
allow_origins=["https://tuempresa.com", "https://www.tuempresa.com"],
'''
class ContactForm(BaseModel):
    nombre: str
    email: str
    mensaje: str
# Validaciones en Backend del Form previstos a futuro.
@app.post("/contact/")
async def recibir_contact(form: ContactForm):
    #recibe un form de tipo ContactForm y sus atr.
    # En MongoDB se podria guardar estos datos.
    print(" Formulariro recibido:", form.dict())
    # en Frontend se puede navegar por el dict de data.datos.nombre
    return {"mensaje": "Gracias por contactarnos", "datos": form.dict()}

@app.get("/contact/")
async def contacto_get():
    return {"mensaje": "Por favor, usa el formulario para enviarnos un mensaje."}