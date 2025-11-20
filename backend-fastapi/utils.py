from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
#.env
from dotenv import load_dotenv
import os
# .env - add .env en gitignore (IMPORTANTE)
# (evita subir el .env a github)
load_dotenv() # CARGA LAS VAR DE .ENV 
SECRET_KEY = os.getenv("SECRET_KEY") #CAMBIAR EN PROD
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",60))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])

def get_hashed_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy() # -> COPIA DEL DICT
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # EXPIRE -> HORA ACTUAL + MINS ACCESS TOKEN EXPIRE
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=str(ALGORITHM))

