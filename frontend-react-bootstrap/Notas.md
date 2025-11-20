
# Introducción del Auth y renderizados sin recargar la pagína.
Cuando hagas login:

- El token se guarda en localStorage.
- El evento storage se dispara.
- El hook useAuth actualiza el estado isLoggedIn a true.
- El navbar muestra "Logout" inmediatamente, sin necesidad de recargar ni navegar.