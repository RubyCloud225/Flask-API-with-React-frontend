import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TrailBalanceTable = () => {
    const [trialBalanceData, setTrialBalanceData] = useState([]);
    const [loading, setloading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedDate, setSelectedDate] = useState(null);

    const handleDateChange = (date) => {
        setSelectedDate(date);
    };

    useEffect(() => {
        const fetchTrialBalanceData = async () => {
            try {
                const response = await axios.get('https://example.com/api/trial-balance');
                setTrialBalanceData(response.data);
                setloading(false);
            } catch (error) {
                setError(error.message);
                setloading(false);
            }
        };
        fetchTrialBalanceData();
    }, []);

    if (loading) {
        return <div>Loading...</div>
    }

    if (error) {
        return <div>Error: {error}</div>;
    }
    return (
        <div>
            <input type="date" value={selectedDate} onChange={(e) => handleDateChange(e.target.value)} />
            {selectedDate && (
                <table>
                <thead>
                    <tr>
                        <th>Account Name</th>
                        <th>Debit</th>
                        <th>Credit</th>
                        <th>Balance</th>
                    </tr>
                </thead>
                <tbody>
                    {trialBalanceData.map((item, index) => (
                        <tr key={index}>
                            <td>{item.accountName}</td>
                            <td>{item.debit}</td>
                            <td>{item.credit}</td>
                            <td>{item.balance}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            )}
        </div>
    );
};

export default TrailBalanceTable;