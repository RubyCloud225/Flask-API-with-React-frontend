import { Row, Col } from 'antd';
import SalesCard from '../../components/dashboard_cards/financecards/SalesCard';
import ExpensesCard from '../../components/dashboard_cards/financecards/ExpensesCard';
import ReportCard from '../../components/dashboard_cards/financecards/ReportsCard';
import BankCard from '../../components/dashboard_cards/financecards/BankCard';

function FinanceDashBoard() {
    return (
        <Row gutter={16}>
            <Col span={6}>
                <SalesCard />
            </Col>
            <Col span={6}>
                <ExpensesCard />
            </Col>
            <Col span={6}>
                <ReportCard />
            </Col>
            <Col span={6}>
                <BankCard />
            </Col>
        </Row>
    );
};

export default FinanceDashBoard;
