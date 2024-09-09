import React, { useState, useEffect } from "react";
import DatePicker from "react-datepicker";

function DiscountedCashFlow() {
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [reportData, setReportData] = useState({});

  useEffect(() => {
    fetch(`/report?start_date=${startDate.toISOString()}&end_date=${endDate.toISOString()}`)
      .then(response => response.json())
      .then(data => setReportData(data));
  }, [startDate, endDate]);

  const handleStartDateChange = date => {
    setStartDate(date);
  };

  const handleEndDateChange = date => {
    setEndDate(date);
  };

  return (
    <div>
      <h2>Discounted Cash Flow Report</h2>
      <div>
        <label>Start Date:</label>
        <DatePicker selected={startDate} onChange={handleStartDateChange} />
      </div>
      <div>
        <label>End Date:</label>
        <DatePicker selected={endDate} onChange={handleEndDateChange} />
      </div>
      {reportData && (
        <div>
          <h3>EBITDA: {reportData.ebitda}</h3>
          <h3>Discounted Cash Flow: {reportData.discounted_cash_flow}</h3>
          <h3>Net Present Value: {reportData.net_present_value}</h3>
        </div>
      )}
    </div>
  );
}

export default DiscountedCashFlow;