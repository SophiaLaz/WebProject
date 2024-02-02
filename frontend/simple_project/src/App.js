import './App.css';
import axios from 'axios';
import React, { useEffect, useState } from "react";

function App() {
  const url_server = "http://localhost:5000/get_actors_list";
  const [actors, setActors] = useState([]);

  useEffect(() => {
    axios
      .get(url_server)
      .then((response) => {
        setActors(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div align="center">
      {actors.map(actor => (
        <div>
          <img src={actor.image} alt={actor.name}/>
          <p>{actor.name}, {actor.info}</p>
          <a
            href={actor.link}
          >
            More information
          </a>
        </div>
      ))}
    </div>
  );
}

export default App;
