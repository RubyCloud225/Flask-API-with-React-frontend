import { Card } from 'antd';

function StockManagementCard() {
    return (
        <Card title="StockManagement" extra={<Link to="/StockManagement">More</Link>}>
            <p>Stock Management</p>
        </Card>
    );
};

export default StockManagementCard;