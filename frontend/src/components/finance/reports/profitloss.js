import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfitLoss = () => {
    const [data, setData] = useState([]);
    const [error, setError] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [categories, setCategories] = useState('');

    useEffect(() => {
        //Fetch catagories from API on mount
        axios.get('api/catagories')
        .then(response => {
            setCategories(response.data)
        })
        .catch(error => {
            setError(error.message);
        });
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('api key', {
            "startDate": startDate,
            "endDate": endDate
        })
        .then(response => {
            setData(response.data);
        })
        .catch(error => {
            setError(error.message);
        });
    };

    return (
        <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
            <h2 style={{ textAlign: 'center' }}>Profit and Loss Statement</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Start Date:</label>
                    <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
                </div>
                <div>
                    <label>End Date:</label>
                    <input type="Date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
                </div>
                <button type="Submit">Submit</button>
            </form>
            {error && (
                <div style={{ marginTop: '10px', padding: '10px', backgroundColor: '#ffcccc', color: '#ff0000'}}>
                    {error}
                </div>
            )}
            {data.length > 0 && (
                <table style={{ width: '100%', border: '1px solid #ddd' }}>
                    <thread>
                        <tr>
                            <th>Date</th>
                            {categories.map((category, index) => (
                                <th key={index}>{category}</th>
                            ))}
                        </tr>
                    </thread>
                    <tbody>
                        {data.map((row, index) => (
                            <tr key={index}>
                                <td>{row.Date}</td>
                                {categories.map((categories, index) => (
                                    <td key={index}>{row[categories]}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default ProfitLoss;