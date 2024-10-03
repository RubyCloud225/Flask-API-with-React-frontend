import { Card } from 'antd';

function ReportCard() {
    return (
        <Card title="Reports" extra={<Link to ="/Reports">More</Link>}>
            <p>Reports</p>
        </Card>
    );
};

export default ReportCard;