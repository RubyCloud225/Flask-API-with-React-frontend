import { Card } from 'antd';

function MarketingCard() {
    return (
        <Card title="Marketing" extra={<Link to ="/marketing">More</Link>}>
            <p>Marketing</p>
        </Card>
    );
};

export default MarketingCard;