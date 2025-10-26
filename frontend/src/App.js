import './App.css';
import React, { useState } from 'react';

// Styles
const errorStyle = {
  color: '#ff6b6b',
  padding: '10px',
  borderRadius: '4px',
  backgroundColor: 'rgba(255, 107, 107, 0.1)',
  border: '1px solid #ff6b6b',
  margin: '10px 0'
};

function FighterAnalysis() {
  const [fighter, setFighter] = useState('');
  const [game, setGame] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8006/api/fighter/${fighter}?game=${game}`);
      const data = await response.json();
      
      // Initialize empty arrays if they're missing
      if (data && !data.error) {
        data.counters = data.counters || [];
        data.victims = data.victims || [];
      }
      
      setAnalysis(data);
    } catch (error) {
      console.error('Error:', error);
      setAnalysis({
        error: 'Failed to analyze fighter. Please try again later.'
      });
    }
    setLoading(false);
  };

  return (
    <div className="fighter-analysis">
      <h2>Fighter Analysis</h2>
      <form onSubmit={handleAnalyze}>
        <div className="form-group">
          <label htmlFor="fighter">Fighter Name:</label>
          <input
            type="text"
            id="fighter"
            value={fighter}
            onChange={(e) => setFighter(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="game">Game (optional):</label>
          <input
            type="text"
            id="game"
            value={game}
            onChange={(e) => setGame(e.target.value)}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Please wait...' : 'Analyze'}
        </button>
      </form>
      
      {loading && (
        <div style={{textAlign: 'center', marginTop: '20px'}}>
          <div className="loading-spinner"></div>
          <p className="loading-text">Analyzing fighter matchups...</p>
          <p style={{fontSize: '0.9rem', color: '#81a1c1'}}>This may take a few moments</p>
        </div>
      )}
      
      {analysis && !loading && (
        <div className="analysis-result">
          {analysis.error ? (
            <p style={errorStyle}>{analysis.error}</p>
          ) : (
            <>
              <h3>{analysis.fighter}</h3>
              <p><strong>Summary:</strong> {analysis.summary}</p>
              {analysis.counters && analysis.counters.length > 0 && (
                <div className="counters">
                  <h4>Weak Against:</h4>
                  <ul>
                    {analysis.counters.map((counter, index) => (
                      <li key={index}>
                        <strong>{counter.name}:</strong> {counter.reason}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              {analysis.victims && analysis.victims.length > 0 && (
                <div className="victims">
                  <h4>Strong Against:</h4>
                  <ul>
                    {analysis.victims.map((victim, index) => (
                      <li key={index}>
                        <strong>{victim.name}:</strong> {victim.reason}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              {analysis.notes && (
                <p><strong>Additional Notes:</strong> {analysis.notes}</p>
              )}
            </>
          )}
        </div>
      )}
    </div>
  );
}

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8006/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
      });
      
      const data = await response.json();
      if (response.ok) {
        setMessage('Login successful!');
        setIsLoggedIn(true);
      } else {
        setMessage(data.message || 'Login failed');
      }
    } catch (error) {
      setMessage('An error occurred. Please try again later.');
    }
  };

  const errorStyle = {
    color: '#ff6b6b',
    padding: '10px',
    borderRadius: '4px',
    backgroundColor: 'rgba(255, 107, 107, 0.1)',
    border: '1px solid #ff6b6b',
    margin: '10px 0'
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Fighter App</h1>
        {!isLoggedIn ? (
          <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
              <div className="form-group">
                <label htmlFor="username">Username:</label>
                <input
                  type="text"
                  id="username"
                  name="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="password">Password:</label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              <button type="submit">Login</button>
            </form>
            {message && <p className="message">{message}</p>}
          </div>
        ) : (
          <FighterAnalysis />
        )}
      </header>
    </div>
  );
}

export default App;



