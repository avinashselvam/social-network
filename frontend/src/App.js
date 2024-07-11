import './App.css';
import Feed from './routes/feed';

import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/feed" element={<Feed />} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
