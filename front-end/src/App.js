import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import FrontPage from "./screens/FrontPage/FrontPage";
import Details from "./screens/Details/Details";
import FeedBack from "./screens/FeedBack/Feedback";
import About from "./screens/About/About";
import Contact from "./screens/Contact/Contact";

export default function App() {
  return (
    <Router>
      {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
      <Switch>
        <Route path="/about">
          <About />
        </Route>
        <Route path="/details">
          <Details />
        </Route>
        <Route path="/feedback">
          <FeedBack />
        </Route>
        <Route path="/contact">
          <Contact />
        </Route>
        <Route path="/">
          <FrontPage />
        </Route>
      </Switch>
    </Router>
  );
}
