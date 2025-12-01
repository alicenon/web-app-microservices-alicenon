# ejemplo de usar el contact de React
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

# TRY AUTH2 30/10/25
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status
from src.contact.infrastructure.database import close_mongo_connection, connect_to_mongo
import utils, database, schemas
from src.contact.api.forms_controller import router as forms_routerv2


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()

# Configura OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI(
    title="Apis de Autenticación y Contacto",
    description="API para autenticación con JWT",
    version="0.1.0",
    # Esto hace que Swagger UI use el método correcto
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    lifespan=lifespan
)
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
#
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# DEFS AUTH 
async def get_current_user(token: str = Depends(oauth2_scheme)):
    creadentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, str(utils.SECRET_KEY), algorithms=[str(utils.ALGORITHM)])
        email: str = payload.get("sub") # -> None SI LA CLAVE NO EXISTE EN EL TOKEN 
        # USAR IF EMAIL IS NONE:RAISE EXCEPT...
        if email is None:
            raise creadentials_exception
    except JWTError:
        raise creadentials_exception
    user = await database.users_collection.find_one({"email": email})
    if user is None:
        raise creadentials_exception
    return user

CurrentUser = Annotated[dict, Depends(get_current_user)]
##RUTAS REGISTRO
@app.post("/register")
async def register(user: schemas.UserCreate):
    existing_user = await database.users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya regristrado")
    
    print(f"Password recibido: {user.password}")  # 👈 Añade esto antes de hashear
    hashed_password = utils.get_hashed_password(user.password)
    new_user = {
        "email": user.email,
        "password": hashed_password
    }
    await database.users_collection.insert_one(new_user)
    return {"message": "¡USUARIO REGISTRADO CON ÉXITO!"}

#RUTAS LOGIN
@app.post("/login")
async def login(form_data: schemas.UserLogin):
    user = await database.users_collection.find_one({"email": form_data.email})
    if not user or not utils.verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Email o contraseña incorrectos")
    
    access_token = utils.create_access_token({"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

#RUTAS PROTEGIDA DE EJEMPLO
@app.get("/perfil")
async def perfil(current_user: CurrentUser):
    return {"email": current_user["email"], "mensaje": "Acceso Permitido"}
    

# ************ Ruta raíz **************
@app.get("/")
def home():
    return {"status": "OK", "mensaje": "Backend corriendo"}
# ************ LOGIN ENDPOINTS***************
# app.post("/register")


# Validaciones en Backend del Form previstos a futuro.
@app.get("/contact/")
async def contacto_get():
    return {"mensaje": "Por favor, usa el formulario para enviarnos un mensaje."}



# ************* FORMS ENDPOINT CLEAN ARCHITECTURE MODE**************
# app.include_router(forms_routerv2)
from src.contact.api.forms_controller import router as contact_router
app.include_router(contact_router, prefix="/contact/v1")
# Fin del archivo main.py
