import React, { useState } from 'react';
import axios from 'axios';

function BalanceSheet() {
    const [asset, setAsset] = useState('');
    const [liability, setLiability] = useState('');
    const [equity, setEquity] = useState('');
    const [balanceSheet, setBalanceSheet] = useState('');
    const [error, setError] = useState=(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/balancesheet', {
                asset,
                liability,
                equity,
            });
            setBalanceSheet(response.data.balanceSheet);
        } catch (error) {
            setError(error.message);
        }
    };
    
    return (
        <div>
            <h1>Balance Sheet</h1>
            <form onSubmit={handleSubmit}>
                <label>
                Assets:
                <input
                    type="number"
                    value={asset}
                    onChange={(e) => setAsset(e.target.value)}
                />
            </label>
            <br />
            <label>
                Liabilities:
                <input
                    type="number"
                    value={liability}
                    onChange={(e) => setLiability(e.target.value)}
                />
            </label>
            <br />
            <label>
                Equity:
                <input
                    type="number"
                    value={equity}
                    onChange={(e) => setEquity(e.target.value)}
                />
            </label>
            <br />
            <button type="submit">Submit</button>
        </form>
        {balanceSheet && <p>Balance Sheet: {balanceSheet}</p>}
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        </div>
    );
}
    
export default BalanceSheet;
