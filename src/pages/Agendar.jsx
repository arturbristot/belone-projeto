import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import "./css/index.css";
import "./css/general.css";



const Agendar = () => {
  const [funcionarios, setFuncionarios] = useState([]);
  const [clientes, setClientes] = useState([]);
  const [barbeiroSelecionado, setBarbeiroSelecionado] = useState("");
  const [clienteSelecionado, setClienteSelecionado] = useState("");
  const [novoCliente, setNovoCliente] = useState("");
  const [observacoes, setObservacoes] = useState("");

  useEffect(() => {
    const buscarFuncionarios = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/funcionarios");
        setFuncionarios(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    const buscarClientes = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/clientes");
        setClientes(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    buscarClientes();
    buscarFuncionarios();
  }, []);

  const handleChange = (event) => {
    const { id, value } = event.target;
    if (id === "barbeiro") {
      setBarbeiroSelecionado(value);
    } else if (id === "Cliente") {
      setClienteSelecionado(value);
    }
  };

  const handleInputChange = (event) => {
    setNovoCliente(event.target.value);
  };

  const handleObservacaoChange = (event) => {
    setObservacoes(event.target.value);
  };

  return (
    <div className="container">
      <h1>Agendar Horario</h1>

      <div className="cadastro">


        <div className="input-group">
          <div className="classe">
            <label htmlFor="barbeiro">Barbeiro:</label>
          </div>
          <select
            id="barbeiro"
            value={barbeiroSelecionado}
            onChange={handleChange}
            className="inp"
          >
            <option value="">Selecione</option>
            {funcionarios.map((funcionario) => (
              <option key={funcionario.id} value={funcionario.id}>
                {funcionario.nome}
              </option>
            ))}
          </select>
        </div>

        <div className="input-group">
          <div className="classe">
            <label htmlFor="Cliente">Cliente:</label>
          </div>
          <select
            id="Cliente"
            value={clienteSelecionado}
            onChange={handleChange}
            className="inp"
          >
            <option value="">Selecione</option>
            {clientes.map((cliente) => (
              <option key={cliente.id} value={cliente.id}>
                {cliente.nome}
              </option>
            ))}
          </select>
        </div>

        <div className="input-group">
          <div className="classe">
            <label htmlFor="novoCliente">Ou digite o nome:</label>
          </div>
          <input
            type="text"
            id="novoCliente"
            value={novoCliente}
            onChange={handleInputChange}
            className="inp"
          />
        </div>

        <div className="input-group">
          <div className="classe">
            <label htmlFor="observacoes">Observações:</label>
          </div>
          <textarea
            id="observacoes"
            value={observacoes}
            onChange={handleObservacaoChange}
            className="inp"
          />
        </div>
        <button className="buttonAdd">Agendar</button>
      </div>
    </div>
  );
};

export default Agendar;
