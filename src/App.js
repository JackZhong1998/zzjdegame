import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CustomContent from './CustomContent';
import GameInterface from './GameInterface';
import UserAccount from './UserAccount';

function App() {
    return (
      <Router>
        <Routes>
          <Route path="/custom-content" element={<CustomContent />} />
          <Route path="/game-interface" element={<GameInterface />} />
          <Route path="/user-account" element={<UserAccount />} />
          <Route path="/" exact element={<Home />} />
        </Routes>
      </Router>
    );
  }

function Home() {
  return <h1>Welcome to the Game Platform</h1>;
}

export default App;