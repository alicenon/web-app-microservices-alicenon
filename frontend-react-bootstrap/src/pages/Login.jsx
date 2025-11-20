import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            //Enviar los datos al Backend
            const response = await axios.post("http://localhost:8000/login", { email, password, });

            //Guardar el token en LocalStorage
            /*MOVER ESTO A UN AuthContext EN UN FUTURO... */
            localStorage.setItem("token", response.data.access_token);
            // DISPARA UN EVENTO PERSONALIZADO
            window.dispatchEvent(new Event('local-storage-changed'));

            navigate('/perfil');//navigate('/');
            //Redirigir a la pág principal o al perfil
            //navigate('/') //EL HOOK DETECTA EL CAMBIO SIN RECARGAR LA PÁGINA
            // window.location.href = '/';
            //Para redirigir a /perfil:
            //navigate("/perfil")

        } catch (err) {
            setError("Email o contraseña incorrectos")
        }
    };
    return (
        <div className="container mt-5">
            <h2>Iniciar Sesión</h2>
            {error && <div className="alert alert-danger">{error}</div>}
            {/* <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Contraseña</label>
                    <input
                        type="password"
                        className="form-control"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" className="btn btn-primary">Iniciar Sesión</button>
            </form> */}

            <form onSubmit={handleSubmit} noValidate>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input
                        type="email"
                        className={`form-control ${error && 'is-invalid'}`} // 👈 Aplica is-invalid si hay un error general
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                    <div className="invalid-feedback">
                        Por favor, introduce un email válido.
                    </div>
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Contraseña</label>
                    <input
                        type="password"
                        className={`form-control ${error && 'is-invalid'}`}
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <div className="invalid-feedback">
                        La contraseña es obligatoria.
                    </div>
                </div>
                <button type="submit" className="btn btn-primary">Iniciar Sesión / Registrarse</button>
            </form>
        </div>
    );
};

export default Login;