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