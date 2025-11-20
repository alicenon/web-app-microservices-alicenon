//  hook que escuche cuando el token se añade o elimina del localStorage y actualice el estado del navbar
// src/hooks/useAuth.js
import { useState, useEffect } from 'react';

export const useAuth = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));

    useEffect(() => {
        // Escucha cambios en localStorage
        const handleStorageChange = () => {
            setIsLoggedIn(!!localStorage.getItem('token'));
        };

        window.addEventListener('storage', handleStorageChange);

        return () => {
            window.removeEventListener('storage', handleStorageChange);
        };
    }, []);

    return isLoggedIn;
};
