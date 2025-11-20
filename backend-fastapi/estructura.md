**Índice**   
1. [Primer apartado](#idv1-0)
2. [Segundo apartado](#idv2-0)
3. [Tercer apartado](#idv3-0)
4. [Cuarto apartado](#idv3-1)
---

<div id='idv1-0'></div>

## v 1... Backend actual <a name="idv1-0"></a>
```zsh
backend/
├── main.py
├── models.py
├── database.py
└── routes/
    └── forms.py
```

<div id='idv2-0'></div>

## v 2... Backend para después <a name="idv2-0"></a>
```zsh

backend/
├── main.py               # Punto de entrada de la API
├── database.py           # Conexión a MongoDB
├── models.py             # Modelos Pydantic (validación, sanitización)
├── routes/               # Rutas separadas por módulo
│   └── forms.py          # Ruta del formulario (Endpoint)
└── .env                  # Variables de entorno (no subir a Git)
```

<div id='idv3-0'></div>

## 📁 v 3.0.0 Estructura final (Clean Architeccccturrrr) 
```zsh
backend/
├── src/                         ← Todo tu código principal
│   ├── auth/                    → Módulo de autenticación
│   │   ├── controller.py        → Rutas FastAPI (login, register, 2FA)
│   │   ├── use_cases.py         → Lógica de negocio (register_user, login_user)
│   │   ├── models.py            → Esquemas Pydantic (UserCreate, Login)
│   │   └── repository.py        → Acceso a DB (MongoDB con Motor)
│   │
│   ├── contact/                 → Módulo de formulario de contacto
│   │   ├── controller.py        → Ruta: /contact
│   │   ├── use_cases.py         → Lógica: enviar email, guardar en DB
│   │   ├── models.py            → Modelo: ContactForm
│   │   └── services.py          → Enviar email (SMTP)
│   │
│   ├── core/                    → Configuración común
│   │   ├── config.py            → Settings con pydantic-settings (.env)
│   │   ├── database.py          → Conexión a MongoDB (Motor)
│   │   └── security.py          → JWT, OAuth2, dependencias
│   │
│   └── main.py                  → Punto de entrada: incluye routers
│
├── tests/                       ← Tus tests (¡aquí es donde brilla!)
│   ├── __init__.py
│   ├── test_auth_use_cases.py   → Prueba la lógica sin levantar el servidor
│   ├── test_contact_use_cases.py
│   └── conftest.py              → Fixtures comunes (db mock, user data)
│
├── .env                         ← Variables de entorno
├── requirements.txt             ← Dependencias
├── Dockerfile                   ← Para contenerizar
└── docker-compose.yml           ← Para levantar todo (MongoDB + backend)
```

<div id='idv3-1'></div>

## v 3.0.1 Estructura final (Clean Architeccccturrrr)
En Python, un directorio se convierte en un paquete si contiene un archivo __init__.py. Esto permite:

- Importar módulos desde subdirectorios.
- Usar rutas relativas como from .auth import login_user
```zsh
backend/
├── src/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── use_cases.py
│   │   ├── models.py
│   │   └── repository.py
│   ├── contact/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── use_cases.py
│   │   ├── models.py
│   │   └── services.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_auth_use_cases.py
│   ├── test_contact_use_cases.py
│   └── conftest.py
├── .env
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```