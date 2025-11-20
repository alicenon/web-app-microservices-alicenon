// src/components/Navbar.js
import React, { useState, useEffect } from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
const NavbarComponent = () => {
    const navigate = useNavigate();
    //VERIFICAR SI HAY TOKEN PARA MOSTRAR "CERRAR SESIÓN"
    // const isLoggedIn = useAuth(); //USAMOS EL HOOK
    const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));

    // Escucha cambios en localStorage
    useEffect(() => {
        const handleStorageChange = () => {
            setIsLoggedIn(!!localStorage.getItem('token'));
        };
        /*MOVER ESTO A UN AuthContext EN UN FUTURO... */
        //ESCUCHA EL EVENT PERSONALIZADO DE LOGIN.JSX
        window.addEventListener('local-storage-changed', handleStorageChange);

        return () => {
            window.removeEventListener('local-storage-changed', handleStorageChange);
        };
        /*FIN MOVER ESTO A UN AuthContext EN UN FUTURO... */
    }, []);
    // const isLoggedIn = useAuth(); // 👈 Usa el hook
    //FUNC ***CERRRAR SESIÓN***
    const handleLogout = () => {
        localStorage.removeItem("token"); //ELIMINA EL TOKEN
        window.dispatchEvent(new Event('local-storage-changed')) //DISPARA EL EVENT
        navigate("/hola")
        // window.location.href = "/hola";
    };


    return (
        <Navbar bg="light" expand="lg" className="mb-4 shadow-sm">
            <Container>
                <Navbar.Brand onClick={() => navigate("/")} className="fw-bold">HESTIA WEB APP</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link onClick={() => navigate("/blog")} >Blog</Nav.Link>
                        <Nav.Link onClick={() => navigate("/product")} >Product</Nav.Link>
                        <Nav.Link onClick={() => navigate("/pricing")} >Pricing</Nav.Link>
                        <Nav.Link onClick={() => navigate("/contact")} >Contact Us</Nav.Link>
                        {/* <Nav.Link href="/signup" className="text-primary fw-semibold">Sign Up</Nav.Link> */}
                    </Nav>
                    <Nav>
                        {isLoggedIn ? (
                            <Nav.Link onClick={handleLogout} className="text-primary fw-semibold">
                                Logout
                            </Nav.Link>
                        ) : (
                            <>
                                <Nav.Link onClick={() => navigate("/signup")} className="text-primary fw-semibold me-3">
                                    Sign Up
                                </Nav.Link>
                                <Nav.Link onClick={() => navigate("/login")} className="text-primary fw-semibold">
                                    Sign In
                                </Nav.Link>
                            </>
                        )}
                    </Nav>

                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default NavbarComponent;