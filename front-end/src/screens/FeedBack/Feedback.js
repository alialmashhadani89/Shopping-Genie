import React from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo3.png";
import feedbackbanner from "../../images/feedback_banner.jpg";
//import "./FeedBack.css";

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
  height: 400
});

const H2 = styled.h2({
  marginTop: 425,
  color: "black",
  marginLeft: -1070
});

const H3 = styled.h3({
  marginTop: 475,
  color: "black",
  marginLeft: -455
});

const H22 = styled.h2({
  margintop: 500,
  marginleft: 700,
  color: "black"
});

const FeedBackPage = () => {
  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <LogoImage src={logo} />
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
        </image>
        <H22>Please fill out the form below.</H22>
        <H2>Do you have something to tell us?</H2>
        <H3>Please send us the direct message through the right box --></H3>
      </Content>
    </MainContainer>
  );
};
export default FeedBackPage;
