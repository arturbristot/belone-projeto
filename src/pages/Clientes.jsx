import React, { useState, useEffect } from "react";
import axios from "axios";
import "./css/index.css";
import "./css/general.css";

import { MdDelete } from "react-icons/md";
import { CiEdit } from "react-icons/ci";

const Clientes = () => {
  const [cliente, setCliente] = useState({
    nome: "",
    telefone: "",
    email: "",
  });
  const [clientes, setClientes] = useState([]);
  const [editando, setEditando] = useState(false);
  const [clienteIdEditando, setClienteIdEditando] = useState(null);

  useEffect(() => {
    const buscarClientes = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/clientes");
        setClientes(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    buscarClientes();
    const intervalId = setInterval(buscarClientes, 1000);

    return () => clearInterval(intervalId);
  }, []);

  async function inserirCliente() {
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/clientes",
        {
          nome: cliente.nome,
          telefone: cliente.telefone,
          email: cliente.email,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log(response.data);
      setClientes([...clientes, response.data]);
      setCliente({ nome: "", telefone: "", email: "" });
    } catch (error) {
      console.error(error);
    }
  }

  async function editarCliente() {
    try {
      const response = await axios.put(
        `http://127.0.0.1:5000/clientes/${clienteIdEditando}`,
        {
          nome: cliente.nome,
          telefone: cliente.telefone,
          email: cliente.email,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.status === 200) {
        setClientes(
          clientes.map((cli) =>
            cli.id === clienteIdEditando ? response.data : cli
          )
        );
        setCliente({ nome: "", telefone: "", email: "" });
        setEditando(false);
        setClienteIdEditando(null);
      }
    } catch (error) {
      console.error(error);
    }
  }

  async function deletarCliente(id) {
    try {
      const response = await axios.delete(
        `http://127.0.0.1:5000/clientes/${id}`
      );

      if (response.status === 200) {
        setClientes(clientes.filter((cliente) => cliente.id !== id));
      }
    } catch (error) {
      console.error(error);
    }
  }

  function iniciarEdicao(cliente) {
    setCliente(cliente);
    setEditando(true);
    setClienteIdEditando(cliente.id);
  }

  return (
    <div className="container">
      <div className="cadastro">
        <h2>{editando ? "Editar Cliente" : "Cadastro de Clientes"}</h2>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="nome">Nome:</label>
          </div>
          <input
            className="inp"
            type="text"
            id="nome"
            name="nome"
            value={cliente.nome}
            onChange={(e) => setCliente({ ...cliente, nome: e.target.value })}
            placeholder="Nome do cliente"
          />
        </div>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="telefone">Telefone:</label>
          </div>
          <input
            className="inp"
            type="text"
            id="telefone"
            name="telefone"
            value={cliente.telefone}
            onChange={(e) =>
              setCliente({ ...cliente, telefone: e.target.value })
            }
            placeholder="Telefone"
          />
        </div>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="email">E-mail:</label>
          </div>
          <input
            className="inp"
            type="email"
            id="email"
            name="email"
            value={cliente.email}
            onChange={(e) => setCliente({ ...cliente, email: e.target.value })}
            placeholder="E-mail"
          />
        </div>

        <button
          className="buttonAdd"
          onClick={editando ? editarCliente : inserirCliente}
        >
          {editando ? "Salvar Alterações" : "Adicionar Cliente"}
        </button>
      </div>

      <div className="listagem">
        <h2>Listagem de clientes</h2>
        <table className="tabela-funcionarios">
          <thead>
            <tr>
              <th>id</th>
              <th>Nome</th>
              <th>Telefone</th>
              <th>Email</th>
              <th className="tacao">Ações</th>
            </tr>
          </thead>
          <tbody>
            {clientes.map((cliente) => (
              <tr key={cliente.id}>
                <td>{cliente.id}</td>
                <td>{cliente.nome}</td>
                <td>{cliente.telefone}</td>
                <td>{cliente.email}</td>
                <td className="acoes">
                  <button
                    className="icon"
                    onClick={() => deletarCliente(cliente.id)}
                  >
                    <MdDelete />
                  </button>
                  <button
                    className="icon"
                    onClick={() => iniciarEdicao(cliente)}
                  >
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

export default Clientes;
