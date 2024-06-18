import React, { useState, useEffect } from "react";
import axios from "axios";
import "./css/index.css";
import "./css/general.css";

import { MdDelete } from "react-icons/md";
import { CiEdit } from "react-icons/ci";

const Agendar = () => {
  const [funcionarios, setFuncionarios] = useState([]);
  const [clientes, setClientes] = useState([]);
  const [agendamentos, setAgendamentos] = useState([]);

  const [agendamento, setAgendamento] = useState({
    funcionarioId: "",
    clienteId: "",
    data: "",
    hora: "",
    observacoes: "",
  });

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

    const buscarAgendamentos = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/agendamentos");
        setAgendamentos(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    buscarClientes();
    buscarFuncionarios();
    buscarAgendamentos();
    const intervalId = setInterval(buscarAgendamentos, 1000);

    return () => clearInterval(intervalId);
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setAgendamento({ ...agendamento, [name]: value });
  };

  async function inserirAgendamento() {
    const dataAgendamento = `${agendamento.data} ${agendamento.hora}:00`;
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/agendamentos",
        {
          cliente_id: agendamento.clienteId,
          funcionario_id: agendamento.funcionarioId,
          servico_id: "1",
          data_agendamento: dataAgendamento,
          observacoes: agendamento.observacoes,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      setAgendamentos([...agendamentos, response.data]);
      setAgendamento({
        funcionarioId: "",
        clienteId: "",
        data: "",
        hora: "",
        observacoes: "",
      });
    } catch (error) {
      console.error("Erro ao inserir agendamento:", error);
    }
  }
  async function deletarAgendamento(id) {
    try {
      const response = await axios.delete(
        `http://127.0.0.1:5000/agendamentos/${id}`
      );

      if (response.status === 200) {
        setClientes(agendamentos.filter((agendamento) => agendamento.id !== id));
      }
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="container">
      <h1>Agendar Horario</h1>

      <div className="cadastro">
        <div className="input-group">
          <div className="classe">
            <label htmlFor="funcionarioId">Barbeiro:</label>
          </div>
          <select
            id="funcionarioId"
            name="funcionarioId"
            value={agendamento.funcionarioId}
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
            <label htmlFor="clienteId">Cliente:</label>
          </div>
          <select
            id="clienteId"
            name="clienteId"
            value={agendamento.clienteId}
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
            <label htmlFor="data">Data:</label>
          </div>
          <input
            type="date"
            id="data"
            name="data"
            value={agendamento.data}
            onChange={handleChange}
            className="inp"
          />
        </div>

        <div className="input-group">
          <div className="classe">
            <label htmlFor="hora">Hora:</label>
          </div>
          <input
            type="time"
            id="hora"
            name="hora"
            value={agendamento.hora}
            onChange={handleChange}
            className="inp"
          />
        </div>

        <div className="input-group">
          <div className="classe">
            <label htmlFor="observacoes">Observações:</label>
          </div>
          <textarea
            id="observacoes"
            name="observacoes"
            value={agendamento.observacoes}
            onChange={handleChange}
            className="inp"
          />
        </div>

        <button className="buttonAdd" onClick={inserirAgendamento}>
          Agendar
        </button>
      </div>
      <div className="listagem">
        <h2>Listagem de agendamentos</h2>
        <table className="tabela-funcionarios">
          {" "}
          {}
          <thead>
            <tr>
              <th>id</th>
              <th>clienteid</th>
              <th>data</th>
              <th>observacoes</th>
              <th className="tacao">Ações</th>
            </tr>
          </thead>
          <tbody>
            {agendamentos.map((agenda) => (
              <tr key={agenda.id}>
                <td>{agenda.funcionario_id}</td>
                <td>{agenda.cliente_id}</td>
                <td>{agenda.data_agendamento}</td>
                <td>{agenda.observacoes}</td>
                <td className="acoes">
                  <button
                    className="icon"
                    onClick={() => deletarAgendamento(agenda.id)}
                  >
                    <MdDelete />
                  </button>{" "}
                  <button className="icon">
                    <CiEdit />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Agendar;
