import React from "react";
import styled from "@emotion/styled";
import aboutbanner from "../../images/about-banner2.png";
import grouppic from "../../images/group-pic.png";
import sallypic from "../../images/sally.jpg";
import stevenpic from "../../images/steven.jpg";
import alipic from "../../images/ali.jpg";

import "./AboutPage.css";

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
  width: 100,
  height: 100
});

const AboutPage = () => {
  return (
    <MainContainer>
      <NavBar>
        <RoutesContainer>
          <RouteItem href="/home">FronPage</RouteItem>
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem selected href="/about">
            Aboutpage
          </RouteItem>
          <RouteItem href="/feedback">FeedBackPage</RouteItem>
          <RouteItem href="/contact">ContactPage</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <image>
          <Image src={aboutbanner} />
          <Image src={grouppic} />
          <Image src={sallypic} />
          <Image src={stevenpic} />
          <Image src={alipic} />
        </image>
      </Content>
    </MainContainer>
  );
};
export default AboutPage;
