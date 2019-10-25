import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import FrontPage from "./screens/FrontPage/FrontPage";
import Details from "./screens/Details/Details";

export default function App() {
  return (
    <Router>
      {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
      <Switch>
        <Route path="/about">
          <FrontPage />
        </Route>
        <Route path="/details">
          <Details />
        </Route>
        <Route path="/feedback">
          <FrontPage />
        </Route>
        <Route path="/contact">
          <FrontPage />
        </Route>
        <Route path="/">
          <FrontPage />
        </Route>
      </Switch>
    </Router>
  );
}
