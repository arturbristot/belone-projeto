import React from 'react';
import { Link } from 'react-router-dom';
import './css/Sidebar.css';


const Sidebar = ({ isOpen, toggleSidebar }) => {
  return (
    <div className={`sidebar-container ${!isOpen ? 'closed' : ''}`}>
      <ul className="sidebar-nav">
        <li className="sidebar-nav-item">
          <Link to="/">Home</Link>
        </li>
        <li className="sidebar-nav-item">
          <Link to="/Agendar">Agendar Horario</Link>
        </li>
        <li className="sidebar-nav-item">
          <Link to="/Clientes">Clientes</Link>
        </li>
        <li className="sidebar-nav-item">
          <Link to="/Funcionarios">Funcionarios</Link>
        </li>
        <li className="sidebar-nav-item">
          <Link to="/Serviços">Serviços</Link>
        </li>
        {/* Adicione mais itens de navegação aqui */}
      </ul>
    </div>
  );
};

export default Sidebar;