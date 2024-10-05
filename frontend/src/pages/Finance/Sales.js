import React, {useState, useEffect } from "react";
import axios from "axios";
import { CSVLink } from "react-csv";

function Sales() {
    const [sales, setSales] = useState([]);
    const [csvData, setCsvData] = useState([]);

    useEffect(()=> {
        axios.get("http://localhost:5000/sales")
        .then(response => {
            setSales(response.data);
            const csvData = response.data.map(sale => [
                sale.id,
                sale.date,
                sale.nominal_id,
                sale.AccountType_id,
                sale.description,
                sale.credit_account,
                sale.credit_amount,
                sale.debit_account,
                sale.debit_amount
            ]);
            setCsvData(csvData);
        })
        .catch(error => {
            console.error(error);
        });
    }, []);

    return (
        <div>
            <h1>Sales List</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nominal ID</th>
            <th>Account Type ID</th>
            <th>Description</th>
            <th>Credit Account</th>
            <th>Credit Amount</th>
            <th>Debit Account</th>
            <th>Debit Amount</th>
          </tr>
        </thead>
        <tbody>
          {sales.map(sale => (
            <tr key={sale.id}>
              <td>{sale.id}</td>
              <td>{sale.user_id}</td>
              <td>{sale.date}</td>
              <td>{sale.nominal_id}</td>
              <td>{sale.AccountType_id}</td>
              <td>{sale.description}</td>
              <td>{sale.credit_account}</td>
              <td>{sale.credit_amount}</td>
              <td>{sale.debit_account}</td>
              <td>{sale.debit_amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <CSVLink data={csvData} filename="sales.csv">
        Export to CSV
      </CSVLink>
    </div>
  );
}

export default Sales;