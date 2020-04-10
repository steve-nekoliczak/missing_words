import React from "react";
import { Route, Switch } from "react-router-dom";

import HomePage from './pages/HomePage';
import StatsPage from './pages/StatsPage';
import HowToPage from './pages/HowToPage';
import UploadPage from './pages/UploadPage';


export default function App() {
  return (
    <Switch>
      <Route exact path="/" component={HomePage}></Route>
      <Route path="/stats" component={StatsPage}></Route>
      <Route path="/how-to" component={HowToPage}></Route>
      <Route path="/upload" component={UploadPage}></Route>
    </Switch>
  );
}
