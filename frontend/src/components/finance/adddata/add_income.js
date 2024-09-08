import React, { useState } from "react";

function RecordIncome() {
    const [date, setDate] = useState("");
    const [description, setDescription] = useState("");
    const [debitAccount, setDebitAccount] = useState("");
    const [debitAmount, setDebitAmount] = useState(0);
    const [creditAccount, setCreditAccount] = useState("");
    const [creditAmount, setCreditAmount] = useState(0);
    const [userId, setUserId] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
    const income = {
        user_id: userId,
        date,
        description,
        debit_account: debitAccount,
        debit_amount: debitAmount,
        credit_account: creditAccount,
        credit_amount: creditAmount
    };
    fetch("/income", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(income)
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                User ID:
                <input type="number" value={userId} onChange={(event) => setUserId(event.target.valueAsNumber)} />
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
                Debit Account:
                <select value={debitAccount} onChange={(event) => setDebitAccount(event.target.value)}>
                    <option value="">Select an account</option>
                    <option value="Bank">Bank</option>
                    <option value="Accounts Receivable">Accounts Receivable</option>
                </select>
            </label>
            <br />
            <label>
                Debit Amount:
                <input type="number" value={debitAmount} onChange={(event) => setDebitAmount(event.target.valueAsNumber)} />
            </label>
            <br />
            <label>
                Credit Account:
                <select value={creditAccount} onChange={(event) => setCreditAccount(event.target.value)}>
                    <option value="">Select an account</option>
                    <option value="Sales">Sales</option>
                    <option value="Service Revenue">Service Revenue</option>
                </select>
            </label>
            <br />
            <label>
                Credit Amount:
                <input type="number" value={creditAmount} onChange={(event) => setCreditAmount(event.target.valueAsNumber)} />
            </label>
            <br />
            <button type="submit">Record Income</button>
        </form>
    );
}

export default RecordIncome;