import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Marketing from './Marketing';
import StockManagement from './StockManagement';
import Finance from './Finance';
import Payroll from './Payroll';
import HR from './HR';

function router() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/Marketing" exact component={Marketing} />
                <Route path="/stock-management" component={StockManagement} />
                <Route path="/finance" component={Finance} />
                <Route path="/payroll" component={Payroll} />
                <Route path="/HR" component={HR} />
            </Switch>
        </BrowserRouter>
    );
};

export default router;

