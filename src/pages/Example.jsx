import { useState } from "react";
import axios from "axios";
//import "./App.css";

function App() {
  const [funcionario, setFuncionario] = useState({
    nome: "",
    especialidade: "",
    telefone: "",
    email: "",
    salario: "",
  });

  async function inserirFuncionario() {
    try {
      const response = await axios.post("http://127.0.0.1:5000/clientes", {
        nome: user.nome,
        especialiadede: user.especialidade,
        telefone: user.telefone,
        email: user.email,
        salario: user.salario,
      }, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
        }}
      >
        <input
          type="text"
          id="nome"
          value={user.nome}
          placeholder="Nome"
          onChange={(e) => setUser({ ...user, nome: e.target.value })}
        />

        <input
          type="text"
          id="telefone"
          value={user.telefone}
          placeholder="Telefone"
          onChange={(e) => setUser({ ...user, telefone: e.target.value })}
        />

        <input
          type="text"
          id="email"
          value={user.email}
          placeholder="Email"
          onChange={(e) => setUser({ ...user, email: e.target.value })}
        />

        <button onClick={inserirUsuario}>Inserir Cliente</button>
      </div>
    </>
  );
}

export default App;
