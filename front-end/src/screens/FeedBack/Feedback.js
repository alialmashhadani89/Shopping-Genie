import React, { useState } from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo15.png";
import feedbackbanner from "../../images/feedback_banner.jpg";

const View = styled.div({
  display: "flex"
});

const Content = styled(View)({
  flex: 1,
  //alignItems: "stretch",
  //flexDirection: "column",
  justifyContent: "flex-start"
});

const MainContainer = styled(View)({
  flex: 1,
  justifyContent: "flex-start",
  alignItems: "stretch",
  flexDirection: "column",
  backgroundColor: "#83d7fe"
});

const NavBar = styled(View)({
  height: 100,
  flexDirection: "row",
  alignItems: "center"
});

const NavBarImageContainer = styled(View)({
  marginLeft: 20
});

const RoutesContainer = styled(View)({
  backgroundColor: "grey",
  flex: 1,
  marginLeft: 20,
  flexDirection: "row",
  justifyContent: "flex-start",
  alignItems: "center"
});

const RouteItem = styled.a(({ selected }) => ({
  padding: "15px 15px",
  backgroundColor: selected ? "orange" : "transparent",
  color: "white",
  "&:hover": {
    backgroundColor: selected ? "orange" : "lightgrey",
    color: selected ? "white" : "green"
  }
}));

const LogoImage = styled.img({
  width: 300,
  height: 135,
  marginTop: 5
});

const Image = styled.img({
  paddingLeft: 20,
  width: 700,
  height: 400,
  marginTop: 25
});

const FeedBackPage = () => {
  const [nameInput, setNameInput] = useState("");
  const [emailInput, setEmailInput] = useState("");
  const [contentInput, setContentInput] = useState("");

  const sendFeedBack = e => {
    e.preventDefault();
    const headers = new Headers();
    headers.append("Content-Type", "application/json");
    fetch("/api/feedbackmail", {
      headers,
      method: "POST",
      body: JSON.stringify({
        name: nameInput,
        email: emailInput,
        content: contentInput
      })
    })
      .then(res => res.json())
      .then(res => {
        alert(res.message);
      });
  };

  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <RouteItem href="/home" style={{ backgroundColor: "transparent" }}>
            <LogoImage src={logo} />
          </RouteItem>
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem href="/home">Home</RouteItem>
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem href="/about">About</RouteItem>
          <RouteItem selected href="/feedback">
            FeedBack
          </RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <image>
          <Image src={feedbackbanner} />
          <h2 style={{ marginLeft: "20px" }}>
            Do you have something to tell us?
          </h2>
          <h3 style={{ marginLeft: "20px" }}>
            Please send us your feed back by filling the from on the right.
          </h3>
        </image>

        <form onSubmit={sendFeedBack} style={{ marginLeft: "50px" }}>
          <h2>Please fill out the form below.</h2>
          <p>Name:</p>
          <input
            type="text"
            onChange={e => setNameInput(e.target.value)}
            style={{ width: "500px", height: "35px" }}
          />
          <p>Email:</p>
          <input
            type="text"
            onChange={e => setEmailInput(e.target.value)}
            style={{ width: "500px", height: "35px" }}
          />
          <p>Message</p>
          <textarea
            onChange={e => setContentInput(e.target.value)}
            rows="15"
            cols="67"
          />
          <p />
          <input type="submit" value="Submit" style={{ width: "100px" }} />
        </form>
      </Content>
    </MainContainer>
  );
};
export default FeedBackPage;
