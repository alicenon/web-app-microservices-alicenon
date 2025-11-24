#de que deberia hacer el test unitario aqui?
from utils import get_hashed_password, verify_password, create_access_token
def test_password_hashing_and_verification():
    password = "mysecretpassword"
    hashed_password = get_hashed_password(password)
    assert verify_password(password, hashed_password) == True
    assert verify_password("wrongpassword", hashed_password) == False
def test_create_access_token():
    data = {"sub": "user1"}
    token = create_access_token(data)
    assert isinstance(token, str) and len(token) > 0
    # Additional checks could include decoding the token and verifying its contents
    from jose import jwt
    from dotenv import load_dotenv
    import os
    load_dotenv()
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_data["sub"] == "user1"
# como ejecuto los test?
# Puedes ejecutar los tests usando pytest. Simplemente guarda este código en un archivo llamado test.py
# y luego ejecuta el siguiente comando en tu terminal:
# pytest test.py
# Asegúrate de tener pytest instalado en tu entorno.
# Puedes instalar pytest usando pip si no lo tienes:
# pip install pytest
# pytest buscará automáticamente las funciones que comienzan con "test_" y las ejecutará.
# explicame que hace cada parte del test.py
# Claro, aquí tienes una explicación de cada parte del código en test.py:
# 1. Importaciones:
#    - from utils import get_hashed_password, verify_password, create_access_token:
#      Esta línea importa las funciones que vamos a probar desde el módulo utils.py.
# 2. test_password_hashing_and_verification():
#    - Esta función prueba las funcionalidades de hashing y verificación de contraseñas.
#    - password = "mysecretpassword": Define una contraseña de prueba.
#    - hashed_password = get_hashed_password(password): Genera un hash de la contraseña
#      utilizando la función get_hashed_password.
#    - assert verify_password(password, hashed_password) == True: Verifica que la
#      contraseña original coincide con el hash generado.
#    - assert verify_password("wrongpassword", hashed_password) == False: Verifica que
#      una contraseña incorrecta no coincide con el hash generado.
# 3. test_create_access_token():
#    - Esta función prueba la funcionalidad de creación de tokens de acceso.
#    - data = {"sub": "user1"}: Define un diccionario con datos de prueba para el token.
#    - token = create_access_token(data): Crea un token de acceso utilizando la función
#      create_access_token.
#    - assert isinstance(token, str) and len(token) > 0: Verifica que el token generado es
#      una cadena no vacía.
#    - from jose import jwt, from dotenv import load_dotenv, import os:
#      Estas líneas importan las bibliotecas necesarias para decodificar el token y cargar
#      las variables de entorno.
#    - load_dotenv(): Carga las variables de entorno desde un archivo .env.
#    - SECRET_KEY = os.getenv("SECRET_KEY"), ALGORITHM = os.getenv("ALGORITHM"):
#      Obtiene la clave secreta y el algoritmo desde las variables de entorno.
#    - decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]): Decodifica el token
#      utilizando la clave secreta y el algoritmo especificados.    
#    - assert decoded_data["sub"] == "user1": Verifica que el contenido decodificado del token
#      coincide con los datos originales proporcionados al crear el token.
# Acuerdate de no repetir porque repites y me haces confundir xD. di un fin o algo asi
# Fin de la explicación del test.py

# Haz el test unitario para el servicio de contacto que esta modolo Clean Architecture
from src.contact.models.models import ContactForm
from src.contact.use_cases.contact_use_case import process_contact_form
import pytest
@pytest.mark.asyncio
async def test_process_contact_form():
    # Datos de prueba para el formulario de contacto
    form_data = {
        "nombre": "Juan Pérez",
        "email": "juan@juan.com",
        "mensaje": "Hola, este es un mensaje de prueba."
    }
    # Crear una instancia de ContactForm con los datos de prueba
    contact_form = ContactForm(**form_data)
    # Llamar al caso de uso para procesar el formulario
    result = await process_contact_form(contact_form)
    # Verificar que el resultado contiene los datos esperados
    assert result["id"] == 1  # Primer formulario guardado
    assert result["email"] == form_data["email"]
    assert result["timestamp"] == "now"
@pytest.mark.asyncio
async def test_process_contact_form_invalid_name():
    # Datos de prueba con un nombre inválido (menos de 3 caracteres)
    form_data = {
        "nombre": "Jo",
        "email": "juan@juan.com",
        "mensaje": "Hola, este es un mensaje de prueba."}
    with pytest.raises(ValueError) as excinfo:
        ContactForm(**form_data)
    assert "El Nombre debe tener al menos 3 caracteres." in str(excinfo.value)
@pytest.mark.asyncio
async def test_process_contact_form_invalid_message():
    # Datos de prueba con un mensaje inválido (menos de 5 caracteres)
    form_data = {
        "nombre": "Juan Pérez",
        "email": "juan@juan.com",
        "mensaje": "Hola"}
    with pytest.raises(ValueError) as excinfo:
        ContactForm(**form_data)
    assert "El Mensaje debe tener al menos 5 caracteres." in str(excinfo.value)
# Fin del test unitario para el servicio de contacto
# Fin del test unitario para el servicio de contacto
# Fin del test unitario para el servicio de contacto. gracias por tu ayuda.
'''
====================================================================================================================== short test summary info ======================================================================================================================= 
FAILED test.py::test_process_contact_form - Failed: async def functions are not natively supported.
FAILED test.py::test_process_contact_form_invalid_name - Failed: async def functions are not natively supported.
FAILED test.py::test_process_contact_form_invalid_message - Failed: async def functions are not natively supported.
Me ayudade a corregir los errores por favor?
Para corregir los errores relacionados con las funciones `async def` en tus pruebas unitarias, necesitas asegurarte de que estás utilizando `pytest-asyncio`, que es un complemento para pytest que permite ejecutar pruebas asíncronas. Aquí te dejo los pasos para corregir los errores:
1. Instala `pytest-asyncio` si no lo tienes ya instalado. Puedes hacerlo ejecutando el siguiente comando en tu terminal:
pip install pytest-asyncio
2. Asegúrate de que estás importando `pytest` correctamente y utilizando el marcador `@pytest.mark.asyncio` para tus funciones de prueba asíncronas, lo cual ya estás haciendo correctamente.
3. Asegúrate de que tu entorno de prueba está configurado para ejecutar pruebas asíncronas. Aquí tienes el código corregido para tus pruebas unitarias:
```

'''