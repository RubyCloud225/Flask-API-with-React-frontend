import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Bank from './bank';
import Sales from './Sales';
import Expenses from './Expenses';
import Reports from './Reports';


function FinanceRouter() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/bank" exact component={Bank} />
                <Route path="/Sales" exact component={Sales} />
                <Route path="./Expenses" exact component={Expenses} />
                <Route path="/Reports" exact component={Reports} />
            </Switch>
        </BrowserRouter>
    );
};

export default FinanceRouter;