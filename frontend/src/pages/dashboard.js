import React from 'react';
import './Dashboard.css';

const Dashboard = () => {
    return (
        <div className="dashboard">
            <div className="row">
                <div className="col-md-3">
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">Marketing</h5>
                            <p className="card-text">Manage your marketing campaigns and strategies.</p>
                            <a href='#' className="btn btn-primary">Go to Marketing</a>
                        </div>
                    </div>
                </div>
                <div className="col-md-3">
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">Stock Management</h5>
                            <p className="card-text">Manage your inventory and stock levels.</p>
                            <a href="#" className="btn btn-primary">Go to Stock Management</a>
                        </div>
                    </div>
                </div>
                <div className="col-md-3">
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">Payroll</h5>
                            <p className="card-text">Manage employee salaries and benefits.</p>
                            <a href="#" className="btn btn-primary">Go to Payroll</a>
                        </div>
                    </div>
                </div>
                <div className="col-md-3">
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">Finance</h5>
                            <p className="card-text">Manage your company's financial transactions and reports.</p>
                            <a href="#" className="btn btn-primary">Go to Finance</a>
                        </div>
                    </div>
                </div>
            </div>
        <div className="row">
            <div className="col-md-3">
                <div className="card">
                    <div className="card-body">
                        <h5 className="card-title">Executive</h5>
                        <p className="card-text">View company performance and make strategic decisions.</p>
                        <a href="#" className="btn btn-primary">Go to Executive</a>
                    </div>
                </div>
            </div>
            <div className="col-md-3">
                <div className="card">
                    <div className="card-body">
                        <h5 className="card-title">HR</h5>
                        <p className="card-text">Manage employee data and benefits.</p>
                        <a href="#" className="btn btn-primary">Go to HR</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    );
};

export default Dashboard;