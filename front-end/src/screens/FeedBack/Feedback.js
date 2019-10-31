import React from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo13.png";
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
  flexDirection: "column"
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
  width: 250,
  height: 100
});

const Image = styled.img({
  paddingLeft: 20,
  width: 700,
  height: 400,
  marginTop: 20
});

const FeedBackPage = () => {
  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <RouteItem href="/home" style={{ backgroundColor: "white" }}>
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

        <form style={{ marginLeft: "50px" }}>
          <h2>Please fill out the form below.</h2>
          <p>Name:</p>
          <input type="text" style={{ width: "500px", height: "35px" }} />
          <p>Email:</p>
          <input type="text" style={{ width: "500px", height: "35px" }} />
          <p>Message</p>
          <textarea rows="18" cols="67" />
        </form>
      </Content>
    </MainContainer>
  );
};
export default FeedBackPage;
