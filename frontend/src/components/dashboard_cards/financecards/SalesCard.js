import { Card } from 'antd';

function SalesCard() {
    return (
        <Card title="Sales" extra={<Link to ="/Sales">More</Link>}>
            <p>Marketing</p>
        </Card>
    );
};

export default SalesCard;