import { Card } from 'antd';

function FinanceCard() {
    return (
        <Card title="Finance" extra={<Link to="/Finance">More</Link>}>
            <p>Finance</p>
        </Card>
    );
};

export default FinanceCard;