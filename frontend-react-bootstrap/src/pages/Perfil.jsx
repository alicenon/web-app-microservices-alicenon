import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Perfil = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                //Obtiene el token del localStorage
                const token = localStorage.getItem("token");

                if (!token) {
                    //SI NO HAY TOKEN, REDIRIGE AL /LOGIN
                    navigate('/login')
                    // window.location.href = "/login" //probar con navigate()
                    return;
                }
                //Hace la petición a /perfil con el token en el header
                const response = await axios.get("http://localhost:8000/perfil", {
                    headers: {
                        "Authorization": `Bearer ${token}`
                    }
                });
                setUser(response.data);
            } catch (err) {
                console.error(err)
                //SI HAY ERROR, PROBABLEMENTE EL TOKEN SEA INVÁLIDO
                localStorage.removeItem("token");
                navigate('/login')
                // window.location.href = "/login";
            } finally {
                setLoading(false);
            }
        };

        fetchProfile();

    }, [navigate]);
    if (loading) {
        return <div>Cargando...</div>;
    }
    return (
        <div className="container mt-5">
            <h2>Tu Perfil</h2>
            {user ? (
                <div>
                    <p><strong>Email: </strong>{user.email}</p>
                    <p><strong>Mensaje: </strong>{user.mensaje}</p>
                </div>
            ) : (
                <p>No se pudo cargar tu perfil.</p>
            )}
        </div>
    );
};
export default Perfil;

/*
🔍 ¿Qué hace este componente?
1. Verifica si hay un token en localStorage.
    - Si no hay token, redirige al login.
2. Hace una petición a /perfil con el token en el header Authorization.
3. Muestra los datos del usuario si la petición es exitosa.
4. Si hay un error, elimina el token y redirige al login.
*/