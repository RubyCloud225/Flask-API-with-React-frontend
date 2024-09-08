import React, { useEffect, useState } from "react";

function AddTransaction() {
    const [date, setDate] = useState("");
    const [description, setDescription] = useState("");
    const [creditAccount, setCreditAccount] = useState("");
    const [creditAmount, setCreditAmount] = useState(0);
    const [debitAccount, setDebitAccount] = useState("");
    const [debitAmount, setDebitAmount] = useState(0);
    const [userId, setUserId] = useState("");
    const [nominals, serNominals] = useState([]);
    const [selectedNominal, setSelectedNominal] = useState('');

    useEffect(() => {
        fetch('/nominals/expense')
        .then(response => response.json())
        .then(data => serNominals(data));
    }, []);

    const handleNominalChange = (event) => {
        setSelectedNominal(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const transaction = {
            user_id: userId,
            date,
            description,
            credit_account: creditAccount,
            credit_amount: creditAmount,
            debit_account: debitAccount,
            debit_amount: debitAmount
        };
        fetch("/transactions", {
            method: "POST",
            headers: { "Content-type": "application/json" },
            body: JSON.stringify(transaction)
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => console.error(error));
    };
    return (
        <form onSubmit={handleSubmit}>
            <label>
                User ID:
                <input type="number" value={userId} onChange={(event) => setUserId(event.target.valueAsNumber)} />
            </label>
            <label>
                Nominal:
                <select value={selectedNominal} onChange={handleNominalChange}>
                    {nominals.map((nominal) => (
                        <option key={nominal.id} value={nominal.code}>
                            {nominal.name}
                        </option>
                    ))}
                </select>
            </label>
            <label>
                Date:
                <input type="date" value={date} onChange={(event) => setDate(event.target.value)} />
            </label>
            <br />
            <label>
                Description:
                <input type="text" value={description} onChange={(event) => setDescription(event.target.value)} />
            </label>
            <br />
            <label>
                Credit Account:
                <select value={creditAccount} onChange={(event) => setCreditAccount(event.target.value)}>
                    <option value="">Select an account</option>
                    <option value="Cash">Cash</option>
                    <option value="Bank">Bank</option>
                    <option value="Accounts Payable">Accounts Payable</option>
                </select>
            </label>
            <br />
            <label>
                Credit Amount:
                <input type="number" value={creditAmount} onChange={(event) => setCreditAmount(event.target.valueAsNumber)} />
            </label>
            <br />
            <label>
                Debit Account:
                <select value={debitAccount} onChange={(event) => setDebitAccount(event.target.value)}>
                    <option value="">Select an account</option>
                    <option value="Cash">Cash</option>
                    <option value="Bank">Bank</option>
                    <option value="Accounts Payable">Accounts Payable</option>
                </select>
            </label>
            <br />
            <label>
                Debit Amount:
                <input type="number" value={debitAmount} onChange={(event) => setDebitAmount(event.target.valueAsNumber)} />
            </label>
            <br />
            <button type="submit">Add Transaction</button>
        </form>
    );
}

export default AddTransaction;