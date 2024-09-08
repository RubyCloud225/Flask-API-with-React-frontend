import React, { useState, useEffect } from 'react';
import DatePicker from 'react-datepicker';

const AgedDebtorsReport = () => {
    const [selectedDate, setSelectedDate ] = useState(new Date());
    const [Data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('https://example.com/api/data');
            const data = await response.json();
            setData(data);
        };
        fetchData();
    }, [selectedDate]);

    const handleDateChange = (date) => {
        setSelectedDate(date);
    };

    return (
        <div>
            <h1>Aged Debtors Report</h1>
            <DatePicker selected={selectedDate} onChange={handleDateChange} dateFormat="yyyy-MM-dd"/>
            <h2>Report Data:</h2>
            <ul>
                {Data.map((item) => (
                    <li key={item.id}>{item.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default AgedDebtorsReport;