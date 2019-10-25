import React from "react";
import { useHistory } from "react-router-dom";
import genie from "../../images/geniegif.gif";
import "./FrontPage.css";

async function submitForm(e, history) {
  e.preventDefault();
  const searchInput = document.getElementById("search-term");
  const searchValue = searchInput.value;
  const new_searchValue = searchValue.trim();
  if (new_searchValue.split(" ").length < 2)
    alert("Please enter more than one keyword.");
  else {
    const results = await fetch(
      "http://localhost:5000/api?search=" + searchValue
    );

    history.push("/details");
  }
}

const FrontPage = () => {
  const history = useHistory();
  return (
    <div className="main-container">
      <header>
        <img
          alt="Genie"
          src={genie}
          width="156"
          height="166"
          align="left"
          style={{
            WebkitTransform: "scaleX(-1)",
            transform: "scaleX(-1)"
          }}
        />
        <img src={genie} width="156" height="166" align="right" />
        <h2>Shopping Genie</h2>
        <br />
        <h3>
          Time & Money in your hands.
          <br />
          Try me and I will gain full control of your day and wallet!
        </h3>
        <ul className="menu">
          <li>
            <a href="index">Home</a>
          </li>
          <li>
            <a href="about">About</a>
          </li>
          <li>
            <a href="feedback">Feedback</a>
          </li>
          <li>
            <a href="contact">Contact</a>
          </li>
        </ul>
      </header>
      <div className="bg">
        <div className="container">
          <form
            onSubmit={e => submitForm(e, history)}
            id="search-form"
            autoComplete="off"
          >
            <div className="input-group">
              <input
                id="search-term"
                type="text"
                className="form-control frontpage-input"
                placeholder="Search Price Genie to save your time and money..."
                name="search"
              />
              <div className="input-group-btn">
                <button className="btn btn-default" type="submit">
                  <i className="glyphicon glyphicon-search"></i>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default FrontPage;
