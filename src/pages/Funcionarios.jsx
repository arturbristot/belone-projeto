import React, { useState, useEffect } from "react";
import axios from "axios";
import "./css/index.css";
import "./css/general.css";

import { MdDelete } from "react-icons/md";
import { CiEdit } from "react-icons/ci";
import { func } from "prop-types";

const Funcionarios = () => {
  const [funcionario, setFuncionario] = useState({
    nome: "",
    especialidade: "",
    telefone: "",
    email: "",
    salario: "",
  });
  const [funcionarios, setFuncionarios] = useState([]);

  useEffect(() => {
    const buscarFuncionarios = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/funcionarios");
        setFuncionarios(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    buscarFuncionarios();
    const intervalId = setInterval(buscarFuncionarios, 500);

    return () => clearInterval(intervalId);
  }, []);

  async function inserirFuncionario() {
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/funcionarios",
        {
          nome: funcionario.nome,
          especialidade: funcionario.especialidade,
          telefone: funcionario.telefone,
          email: funcionario.email,
          salario: funcionario.salario,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log(response.data);
      // Após inserir, atualiza a lista:
      setFuncionarios([...funcionarios, response.data]);
    } catch (error) {
      console.error(error);
    }
  }

  async function deletarFuncionario(id) {
    try {
      const response = await axios.delete(
        `http://127.0.0.1:5000/funcionarios/${id}`
      );

      if (response.status === 200) {
        setFuncionarios(
          funcionarios.filter((funcionario) => funcionario.id !== id)
        );
      }
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="container">
      <div className="cadastro">
        <h2>Cadastro de Funcionários</h2>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="">Nome:</label>
          </div>
          <input
            className="inp"
            type="text"
            id="nome"
            name="nome"
            value={funcionario.nome}
            onChange={(e) =>
              setFuncionario({ ...funcionario, nome: e.target.value })
            }
            placeholder="Nome do funcionário"
          />
        </div>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="">Especialidade:</label>
          </div>
          <input
            className="inp"
            type="text"
            id="especialidade"
            name="especialidade"
            value={funcionario.especialidade}
            onChange={(e) =>
              setFuncionario({ ...funcionario, especialidade: e.target.value })
            }
            placeholder="Especialidade"
          />
        </div>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="">Telefone:</label>
          </div>
          <input
            className="inp"
            type="text"
            id="telefone"
            name="telefone"
            value={funcionario.telefone}
            onChange={(e) =>
              setFuncionario({ ...funcionario, telefone: e.target.value })
            }
            placeholder="Telefone"
          />
        </div>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="">E-mail:</label>
          </div>

          <input
            className="inp"
            type="email"
            id="email"
            name="email"
            value={funcionario.email}
            onChange={(e) =>
              setFuncionario({ ...funcionario, email: e.target.value })
            }
            placeholder="E-mail"
          />
        </div>
        <div className="input-group">
          <div className="classe">
            <label htmlFor="">Salário:</label>
          </div>
          <input
            className="inp"
            type="number"
            id="salario"
            name="salario"
            value={funcionario.salario}
            onChange={(e) =>
              setFuncionario({ ...funcionario, salario: e.target.value })
            }
            placeholder="Salário"
          />
        </div>

        <button className="buttonAdd" onClick={inserirFuncionario}>
          Adicionar Funcionário
        </button>
      </div>

      <div className="listagem">
        <h2>Listagem de Funcionários</h2>
        <table className="tabela-funcionarios">
          {" "}
          {/* Adicione uma classe à tabela */}
          <thead>
            <tr>
              <th>id</th>
              <th>Nome</th>
              <th>Especialidade</th>
              <th>Telefone</th>
              <th>Email</th>
              <th>Salário</th>
              <th className="tacao">Ações</th>
            </tr>
          </thead>
          <tbody>
            {funcionarios.map((funcionario) => (
              <tr key={funcionario.id}>
                <td>{funcionario.id}</td>
                <td>{funcionario.nome}</td>
                <td>{funcionario.especialidade}</td>
                <td>{funcionario.telefone}</td>
                <td>{funcionario.email}</td>
                <td>{funcionario.salario}</td>
                <td className="acoes">
                  <button
                    className="icon"
                    onClick={() => deletarFuncionario(funcionario.id)}
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

export default Funcionarios;
