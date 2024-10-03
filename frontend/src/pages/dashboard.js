import { Row, Col } from 'antd';
import MarketingCard from './components/dashboard_cards/homecards/MarketingCard';
import StockManagementCard from './components/dashboard_cards/homecards/StockManagementCard';
import FinanceCard from './components/dashboard_cards/homecards/FinanceCard';
import PayrollCard from './components/dashboard_cards/homecards/PayrollCard';
import HRCard from './HRCard';

function Dashboard() {
    return (
        <Row gutter={16}>
            <Col span={6}>
                <MarketingCard />
            </Col>
            <Col span={6}>
                <StockManagementCard />
            </Col>
            <Col span={6}>
                <FinanceCard />
            </Col>
            <Col span={6}>
                <PayrollCard />
            </Col>
            <Col span={6}>
                <HRCard />
            </Col>
        </Row>
    );
};

export default Dashboard;
