import { Card } from 'antd';

function BankCard() {
    return (
        <Card title="Bank" extra={<Link to ="/Bank">More</Link>}>
            <p>Bank</p>
        </Card>
    );
};

export default BankCard;