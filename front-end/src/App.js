import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import FrontPage from "./screens/FrontPage/FrontPage";
import Details from "./screens/Details/Details";
import FeedBackPage from "./screens/FeedBackPage/FeedbackPage";
import AboutPage from "./screens/AboutPage/AboutPage";
import ContactPage from "./screens/ContactPage/ContactPage";

export default function App() {
  return (
    <Router>
      {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
      <Switch>
        <Route path="/about">
          <AboutPage />
        </Route>
        <Route path="/details">
          <Details />
        </Route>
        <Route path="/feedback">
          <FeedBackPage />
        </Route>
        <Route path="/contact">
          <ContactPage />
        </Route>
        <Route path="/">
          <FrontPage />
        </Route>
      </Switch>
    </Router>
  );
}
