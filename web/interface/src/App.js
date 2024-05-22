import logo from './logo.svg';
import './App.css';
import Topo from './componentes/Topo';
import SearchableTable from './componentes/Table';

const data = [    {
  "file_name": "audios/c.2024-05-06@0700.wav",
  "send_telegram": true,
  "timestamp": "Mon, 06 May 2024 07:01:03 GMT",
  "transcription": " Tchau, tchau, tchau. "
},
{
  "file_name": "audios/c.2024-05-06@0658.wav",
  "send_telegram": true,
  "timestamp": "Mon, 06 May 2024 06:59:23 GMT",
  "transcription": " Tchau. "
}];

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Topo projectName="Radio Esculta" />
      <SearchableTable data={data} />

      </header>
    </div>
  );
}

export default App;
