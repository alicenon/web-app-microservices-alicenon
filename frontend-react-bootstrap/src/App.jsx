// import logo from './logo.svg';
// import './App.css';
// src/App.js
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavbarComponent from './components/NavbarComponent';
import MyFooter from './components/Footer';
import Home from './pages/Home';
import Blog from './pages/Blog';
import Product from './pages/Product';
import Pricing from './pages/Pricing';
import Contact from './pages/Contact';
import Login from './pages/Login';
import Perfil from './pages/Perfil';
import Signup from './pages/Signup';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
function App() {
  return (
    <Router>
      {/* Contien el menu de navegacion */}
      <NavbarComponent />
      {/* Este es el enrutador de las pages */}
      <div className='container'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/blog" element={<Blog />} />
          <Route path="/product" element={<Product />} />
          <Route path="/pricing" element={<Pricing />} />
          <Route path="/contact" element={<Contact />} />
          {/* Login: add component Login, Perfil */}
          <Route path="/login" element={<Login />} />
          <Route path="/perfil" element={<Perfil />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </div>
      {/* Este es el componente pie de pagine */}
      <MyFooter></MyFooter>
    </Router>

  );
}
export default App;
