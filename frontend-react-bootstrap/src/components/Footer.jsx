import { Link } from "react-router-dom";

//Componente Pie de Página - Reutilizable para todas las pages/
const footerComponent = () => {
    // const navigate = useNavigate;
    return (
        <footer className="bg-light text-center text-muted py-4 mt-5 border-top">
            <div className="container">
                <p className="mb-1">© 2025 Hestia. All rights reserved.</p>
                <small>
                    <Link to="/privacy" className="text-muteed m-3">Privacy policy/</Link>
                    <Link to={"/terms"} className="text-muteed">Terms and Contitions of Service</Link>
                </small>

            </div>
        </footer >
    );
}

export default footerComponent;