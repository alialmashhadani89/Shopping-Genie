import React from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo13.png";
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
  float: "left",
  marginLeft: 30
});
const Image2 = styled.img({
  width: 500,
  height: 400,
  float: "right",
  marginRight: 70
});

const ImageAli = styled.img({
  width: 300,
  height: 400,
  float: "left",
  marginLeft: 40,
  marginTop: 30
});

const ImageSteven = styled.img({
  width: 300,
  height: 400,
  float: "center",
  marginTop: 40,
  marginLeft: 250
});

const ImageSally = styled.img({
  width: 300,
  height: 400,
  float: "right",
  marginTop: 40,
  marginRight: 150
});

const TextAli = styled.text({
  float: "left",
  marginLeft: 40
});

const TextSteven = styled.text({
  float: "left",
  marginLeft: 160
});

const TextSally = styled.text({
  float: "right",
  marginRight: 50
});

const LogoImage = styled.img({
  width: 250,
  height: 100
});

const AboutPage = () => {
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
          <RouteItem selected href="/about">
            About
          </RouteItem>
          <RouteItem href="/feedback">FeedBack</RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <text style={{ marginLeft: 30, marginTop: 40 }}>
          <h2>
            <b> Who We Are? </b>
          </h2>
          <h3> We are developers, problem-solvers, and challengers!</h3>
        </text>
        <image>
          <Image src={grouppic} style={{ marginTop: 45 }} />
          <Image2 src={aboutbanner} style={{ marginTop: 45 }} />
        </image>

        <image>
          <ImageAli src={alipic} />
          <ImageSteven src={stevenpic} />
          <ImageSally src={sallypic} />
        </image>
        <text>
          <TextAli>
            <b>
              <h2>Ali Almashhadani</h2>
              <h3>[Back-End Developer & AI,Database]</h3>
            </b>
          </TextAli>
          <TextSteven>
            <b>
              <h2>Steven Santana</h2>
              <h3>[Back-End Developer & Database]</h3>
            </b>
          </TextSteven>
          <TextSally>
            <b>
              <h2>Sally Xuan</h2>
              <h3>[Front-End Developer & QA Engineer]</h3>
            </b>
          </TextSally>
        </text>
      </Content>
    </MainContainer>
  );
};
export default AboutPage;
