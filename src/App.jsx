import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import "./App.css";

import Home from "./pages/Home";
import Agendar from "./pages/Agendar";
import Clientes from "./pages/Clientes";
import Funcionarios from "./pages/Funcionarios";
import Servicos from "./pages/Servicos";

function App() {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} /> 
            <Route path="/Agendar" element={<Agendar />} />
            <Route path="/Clientes" element={<Clientes />} />
            <Route path="/Funcionarios" element={<Funcionarios />} />
            <Route path="/Serviços" element={<Servicos />} />
          </Routes>
        </div>
        
      </div>
    </Router>
  );
}

export default App;
