// usado par avalidaciones cambios de variables, etc
import { useState } from "react";
// initialData porque no sabemos cuantos datos tiene el form
const useForm = (initialData) => {
    const [form, setForm] = useState(initialData);
    const [loading, setLoading] = useState(false);

    // 2 func para cuando queramos cambiar campos cuando enviemos el form
    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm({ ...form, [name]: value });
    }

    const handleSubmit = (onSubmit) => async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            await onSubmit(form); // Llama a tu función de envío
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    }
    // retorna 4 var las dos de estados y las dos func . reutilizables. 
    return { form, loading, handleChange, handleSubmit }

}

export default useForm;