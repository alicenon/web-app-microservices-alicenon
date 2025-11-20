// src/pages/Signup.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Signup = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Envía los datos al backend FastAPI
            await axios.post('http://localhost:8000/register', {
                email,
                password
            });

            // Si todo va bien, redirige al login
            navigate('/login'); //EL HOOK DETECTA EL CAMBIO SIN RECARGAR LA PÁGINA
        } catch (err) {
            // Muestra un mensaje si el email ya está registrado
            setError('Error al registrar. ¿El email ya existe?');
        }
    };

    return (
        <div className="container mt-5">
            <h2>Crear cuenta</h2>
            {error && <div className="alert alert-danger">{error}</div>}
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email</label>
                    <input
                        type="email"
                        className={`form-control ${error ? 'is-invalid' : ''}`}
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
                        className={`form-control ${error ? 'is-invalid' : ''}`}
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <div className="invalid-feedback">
                        La contraseña es obligatoria.
                    </div>
                </div>
                <button type="submit" className="btn btn-primary">Registrarse</button>
            </form>
        </div>
    );
};

export default Signup;