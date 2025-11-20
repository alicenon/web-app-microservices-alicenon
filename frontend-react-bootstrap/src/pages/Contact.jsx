import userForm from '../hooks/useForm';
// este import ahora mueve la logica el usetate que usaba aqui a ..hooks/useForm
// src/pages/Contact.js
import { useState } from 'react';

export default function Contact() {

    /**
     * Usando validación en react
     * ubicación: ../hooks/useForm
     * descripción: removido la logica de useState de este componente y ahora en otra ubicación para mejorar modularidad.
     */
    const initialData = {
        // prop del form
        nombre: '',
        email: '',
        mensaje: ''
    }
    const { form, loading, handleChange, handleSubmit } = userForm(initialData);
    // console.log(form);
    const enviarDatos = async (datos) => {
        try {
            const res = await fetch('http://localhost:8000/forms/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(datos)
            });

            if (res.ok) {
                // const data_backend = await res.json();
                // alert("¡Gracias por tu mensaje!" + data_backend.nombre);
                alert('¡Gracias por tu mensaje!');

                // Opcional pero se podria resetear el formulario aquí
            } else {
                alert('Error al enviar.');
            }
        } catch (err) {
            alert('Error de conexión.');
        }
    };
    // const [formData, setFormData] = useState({
    //     nombre: '',
    //     email: '',
    //     mensaje: ''
    // });

    /*
        const handleChange1 = (e) => {
            setFormData({ ...formData, [e.target.name]: e.target.value });
        };
    
        const handleSubmit1 = async (e) => {
            e.preventDefault();
            try {
                // NO OLVIDAR EN BACKEND VALIDAR EL CORS!!!
                const res = await fetch('http://localhost:8000/contact/', {
                    method: 'POST',
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(formData)//convierte el objeto formData en JSON
    
                });
                if (res.ok) {
                    alert("¡Formulario enviado!");
                    const data = await res.json(); // 🔥 Aquí recibes el mensaje de FastAPI
                    alert(data.mensaje + data.datos.nombre); // 👉 "Gracias por contactarnos. Tu mensaje ha sido enviado."
                    setFormData({ nombre: "", email: "", mensaje: "" });
                }
            } catch (err) {
                alert("Error al enviar datos del FORM")
            }
            // alert('Formulario enviado! (Simulado)');
            // Aquí iría la llamada a tu backend FastAPI
            // await fetch('/api/contact', { method: 'POST', body: JSON.stringify(formData) })
            // setFormData({ nombre: '', email: '', mensaje: '' });
        };*/

    return (
        <div className="container my-5">
            <h2 className="text-center mb-4">Contact Us</h2>
            <div className="row justify-content-center">
                <div className="col-md-8">
                    <div className="card shadow-sm">
                        <div className="card-body p-4">
                            <form onSubmit={handleSubmit(enviarDatos)}>
                                <div className="mb-3">
                                    <label className="form-label">Nombre</label>
                                    <input
                                        type="text"
                                        name="nombre"
                                        className="form-control"
                                        value={form.nombre}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label className="form-label">Email</label>
                                    <input
                                        type="email"
                                        name="email"
                                        className="form-control"
                                        value={form.email}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label className="form-label">Mensaje</label>
                                    <textarea
                                        name="mensaje"
                                        className="form-control"
                                        rows="6"
                                        value={form.mensaje}
                                        onChange={handleChange}
                                        required
                                    ></textarea>
                                </div>
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className="btn btn-primary w-100"
                                >
                                    {loading ? 'Enviando...' : 'Enviar'}
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
