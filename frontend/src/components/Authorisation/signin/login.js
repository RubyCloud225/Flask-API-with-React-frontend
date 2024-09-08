import React, { useState } from 'react';

const LoginScreen = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then((data) => {
            if (data.success) {
                window.location.href = '/dashboard';
            } else {
                setError(data.error);
            }
        })
        .catch((error) => {
            setError('Anerror occurred, please try again later');
        });
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <label>Username:</label>
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                <br />
                <label>Password:</label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <br />
                {error && <div style={{ color: 'red' }}>{error}</div>}
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default LoginScreen;