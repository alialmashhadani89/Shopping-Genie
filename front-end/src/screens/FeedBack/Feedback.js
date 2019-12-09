import React, { useState } from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo15.png";
import backgroundpic from "../../images/feedback.jpg";

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
  backgroundImage: `url(${backgroundpic})`,
  backgroundSize: "cover",
  overflow: "hidden",
  backgroundRepeat: "no-repeat",
  backgroundPosition: "center"
});

const NavBar = styled(View)({
  height: 100,
  flexDirection: "row",
  alignItems: "center",
  marginTop: "10px"
});

const NavBarImageContainer = styled(View)({
  marginLeft: 20
});

const RoutesContainer = styled(View)({
  //backgroundColor: "grey",
  flex: 1,
  marginLeft: 20,
  flexDirection: "row",
  justifyContent: "flex-start",
  alignItems: "center"
});

const RouteItem = styled.a(({ selected }) => ({
  padding: "20px 20px",
  //backgroundColor: selected ? "orange" : "transparent",
  color: "white"
  //"&:hover": {
  // backgroundColor: selected ? "orange" : "transparent",
  // color: selected ? "white" : "green"
  //}
}));

const LogoImage = styled.img({
  width: 300,
  height: 135,
  marginTop: 5
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
        document.getElementById("inputname").value = "";
        document.getElementById("inputemail").value = "";
        document.getElementById("inputtext").value = "";
      });
  };

  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <RouteItem href="/home">
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
        <h2 style={{ marginLeft: "60px", color: "#42f5f5" , marginTop:"500px"}}>
          <p>Do you have something to tell us?</p>

          <p>Please send us your feed back by</p>
          <p>filling the form on the right.</p>
        </h2>

        <form
          onSubmit={sendFeedBack}
          style={{ marginLeft: "320px", marginRight: "20PX", color: "#42f5f5" ,marginTop:"70px"}}
        >
          <h2>Please Fill Out the Form Below.</h2>
          <p>Name:</p>
          <input
            id="inputname"
            type="text"
            onChange={e => setNameInput(e.target.value)}
            style={{ width: "500px", height: "35px", color: "black" }}
          />
          <p></p>
          <p>Email:</p>
          <input
            id="inputemail"
            type="text"
            onChange={e => setEmailInput(e.target.value)}
            style={{ width: "500px", height: "35px", color: "black" }}
          />
          <p></p>
          <p>Message:</p>
          <textarea
            id="inputtext"
            onChange={e => setContentInput(e.target.value)}
            style={{ width: "500px", color: "black" }}
            rows="15"
            cols="67"
          />
          <p />
          <input
            type="submit"
            value="Submit"
            style={{ width: "100px", color: "black" }}
          />
        </form>
      </Content>
    </MainContainer>
  );
};
export default FeedBackPage;
