import React, { useState } from 'react';
import { Modal, Button } from 'react-bootstrap';
import { countries } from './countries';

function SignUp() {
    const [username, setUsername] = useState('');
    const [companyName, setCompanyName] = useState('');
    const [country, setCountry] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showSignUp, setShowSignUp] = useState(false);
    const [passwordError, setPasswordError] = useState(null);

    const validatePassword = (password) => {
        if (password.length < 8) return false;
        if (!/[a-z]/.test(password)) return false;
        if (!/[A-Z]/.test(password)) return false;
        if (!/[0-9]/.test(password)) return false;
        if (!/[_@$]/.test(password)) return false;
        return true;
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const userData = {
            username, 
            companyName,
            country,
            email,
            password,
            confirmPassword,
        };
        if (password !== confirmPassword) {
            setPasswordError('Passwords do not match');
        } else if (!validatePassword(password)) {
            setPasswordError('Passwords must be leasst 8 characters, include a capital letter, a digit, and a symbol');
        } else {
            fetch('/api/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/login';
                } else {
                    setPasswordError(data.error);
                }
            })
            .catch(error => {
                setPasswordError('An error occured, please try again later');
            });
        };
    }
    const handleSignUpClose = () => setShowSignUp(false);
    const handleSignUpShow = () => setShowSignUp(true);

    return (
        <div>
            <Button variant="primary" onClick={handleSignUpShow}>
                Sign Up
            </Button>
            <Modal show={showSignUp} onHide={handleSignUpClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Sign Up</Modal.Title>
                </Modal.Header>
                    <Modal.Body>
                        <form onSubmit={handleSubmit}>
                            <label>Username:</label>
                            <input type="text" value={username} onChange={(event) => setUsername(event.target.value)}/>
                            <br />
                            <label>Company Name:</label>
                            <input type="text" value={companyName} onChange={(event) => setCompanyName(event.target.value)} />
                            <br />
                            <label>Company Country Location:</label>
                            <select value={country} onChange={(event) => setCountry(event.target.value)}>
                                {countries.map((country, index) => (
                                    <option key={index} value={country.name}>{country.name}</option>
                                ))}
                            </select>
                            <br />
                            <label>Email:</label>
                            <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
                            <br />
                            <label>Password:</label>
                            <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
                            <br />
                            <label>Confirm Password:</label>
                            <input type="password" value={confirmPassword} onChange={(event) => setConfirmPassword(event.target.value)} />
                            <br />
                            {passwordError && <div style={{ color: 'red' }} > {passwordError}</div>}
                            <Button variant="primary" type="submit">
                                Sign Up
                            </Button>
                        </form>
                    </Modal.Body>
            </Modal>
        </div>
    );
};

export default SignUp;