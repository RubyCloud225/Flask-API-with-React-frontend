import { Card } from 'antd';

function HRCard() {
    return (
        <Card title="HR" extra={<Link to="/HR">More</Link>}>
            <p>HR Function</p>
        </Card>
    );
};

export default HRCard;