import './App.css';
import photo from './Lee Dong-wook.jpeg'

function App() {
  return (
    <div id="actor" align="center">
        <img src={photo} alt="Lee Dong-wook" />
        <p>
          Lee Dong-wook, born November 6, 1981.
        </p>
        <a
          href="https://www.kinopoisk.ru/name/1282438/?utm_referrer=yandex.ru"
        >
          More information
        </a>
    </div>
  );
}

export default App;
