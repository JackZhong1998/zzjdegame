import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CustomContent from './CustomContent';
import GameInterface from './GameInterface';
import UserAccount from './UserAccount';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/custom-content" component={CustomContent} />
                <Route path="/game-interface" component={GameInterface} />
                <Route path="/user-account" component={UserAccount} />
                <Route path="/" exact component={Home} />
            </Switch>
        </Router>
    );
}

function Home() {
    return <h1>Welcome to the Game Platform</h1>;
}

export default App;