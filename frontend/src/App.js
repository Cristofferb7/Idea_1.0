import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState(''); 
  const [message, setMessage] = useState('');
  const handleLogin = async(e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          body: JSON.stringify({ username, password }), 
        },
      });
      const data = await response.json(); 
      if (response.ok) {
        setMessage('Login successful!');
      } else {
        setMessage(data.message || 'Login failed');
      } 
    } catch (error) {
      setMessage('An error occurred. Please try again later.');
    }
  return (
    <div className="App">
      <header>AI Fighter App</header>
      <h1>AI Fighter App</h1>
      <h2>Login</h2>
      <form>
        <label>Enter Username
          <input type="text" name="username" value={username} onChange={(e) =>setUsername(e.target.value)}/>
        </label>
        <br />
        <label>Enter Password
          <input type="password" name="password" value={password} onChange={(e) =>setPassword(e.target.value)}/>
        </label>
      </form>
    <button type='submit'>login</button>
    </div>
    
  
  );
}
}

export default App;
