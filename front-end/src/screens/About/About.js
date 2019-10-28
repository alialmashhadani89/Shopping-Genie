import React from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo6.png";
import aboutbanner from "../../images/about-banner2.png";
import grouppic from "../../images/group-pic.png";
import sallypic from "../../images/sally.jpg";
import stevenpic from "../../images/steven.jpg";
import alipic from "../../images/ali.jpg";

const View = styled.div({
  display: "flex"
});

const Content = styled(View)({
  flex: 1,
  alignItems: "stretch",
  flexDirection: "column",
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

const Image = styled.img({
  width: 500,
  height: 400,
  float: "right",
  marginLeft: 400
});
const Image2 = styled.img({
  width: 500,
  height: 400,
  float: "left",
  marginRight: -200
});

const LogoImage = styled.img({
  width: 250,
  height: 100
});

const H4 = styled.h4({
  color: "black",
  marginRight: "50"
});

const AboutPage = () => {
  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <LogoImage src={logo} />
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem href="/home">Home</RouteItem>
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem selected href="/about">
            About
          </RouteItem>
          <RouteItem href="/feedback">FeedBack</RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <H4>
          <h4> Who We Are? </h4>
          <h4> We are developers, problem-solvers, and challengers!</h4>
        </H4>
        <image>
          <Image src={aboutbanner} />
          <Image2 src={grouppic} />
        </image>
      </Content>
    </MainContainer>
  );
};
export default AboutPage;
